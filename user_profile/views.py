from django.contrib import messages
from django.shortcuts import render, redirect
from .models import UserIMT
from .forms import UserProfileForm, UserProfileUpdateForm


# Create your views here.
def view_profile(request):
    return render(request, 'user_profile/view_profile.html')


def edit_profile(request):
    user = request.user
    profile = user.userprofile

    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST,
                                     instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль успешно обновлен')
            return redirect(to='user_profile:view_profile')
    else:
        form = UserProfileUpdateForm(instance=profile)

    return render(request, 'user_profile/edit_profile.html', {'form': form})


def fill_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user  # Присваиваем текущего пользователя
            profile.save()
            return redirect(to='user_profile:view_profile')  # Перенаправляем на страницу профиля
    else:
        form = UserProfileForm()

    return render(request, 'user_profile/fill_profile.html', {'form': form})


def imt(request):
    user = request.user
    profile = user.userprofile
    weight = profile.weight
    height = profile.height / 100
    imt_value = weight / pow(height, 2)
    imt_value = round(imt_value, 1)

    if imt_value < 18.5:
        status = 'Недостаточный'
    elif 18.5 <= imt_value < 25:
        status = 'Нормальный'
    elif 25 <= imt_value < 30:
        status = 'Избыточный'
    else:
        status = 'Ожирение'

    try:
        user_imt = UserIMT.objects.get(user=user)
        user_imt.value = imt_value
        user_imt.status = status
        user_imt.save()
    except UserIMT.DoesNotExist:
        UserIMT.objects.create(user=user, value=imt_value, status=status)

    profile = user.userprofile
    formula = 9.99 * profile.weight + 6.25 * profile.height - 4.92 * profile.age
    if profile.sex == 1:
        # man
        formula += 5
    else:
        # woman
        formula -= 161

    formula *= profile.activity_level
    recommended_calories = round(formula)
    if status == 'Недостаточный':
        recommended_calories = round(recommended_calories + recommended_calories * 0.2)
    if status == 'Избыточный' or status == 'Ожирение':
        recommended_calories = round(recommended_calories - recommended_calories * 0.2)
    else:
        if profile.scope == 'weight_loss':
            recommended_calories = round(recommended_calories - recommended_calories * 0.2)
        elif profile.scope == 'muscle_gain':
            recommended_calories = round(recommended_calories + recommended_calories * 0.2)

    user_imt = UserIMT.objects.get(user=user)
    user_imt.recommended_calories = recommended_calories
    user_imt.save()

    return render(request, 'user_profile/imt.html')
