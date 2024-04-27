from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import LoginForm, UserRegistrationForm
from product.models import Cart


# Create your views here.
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)  # User obj is created, but not is saved
            cd = user_form.cleaned_data
            new_user.set_password(cd['password'])  # setting chosen password
            new_user.save()  # saving User
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(to='home:home')

                else:
                    return HttpResponse("Disabled account")
            else:
                return HttpResponse("Invalid login")
    else:
        user_form = UserRegistrationForm()
    return render(request, 'home/register.html', {'user_form': user_form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(to='home:home')

                else:
                    return HttpResponse("Disabled account")
        else:
            return HttpResponse("Invalid login")
    else:
        form = LoginForm
    return render(request, 'home/login.html', {'form': form})


def home(request):
    if request.user.is_authenticated:
        try:
            user_cart = Cart.objects.get(user=request.user)
            consumed_water = user_cart.total_water
            daily_needed_water = 2400
            water_percentage = round((int(consumed_water) / daily_needed_water) * 100)
            total_proteins = round(user_cart.total_protein)
            total_lipids = round(user_cart.total_lipids)
            total_carbohydrates = round(user_cart.total_carbohydrates)
            return render(request, 'home/home.html',
                          {'consumed_water': consumed_water,
                           'water_percentage': water_percentage,
                           'user_cart': user_cart,
                           'total_proteins': total_proteins,
                           'total_lipids': total_lipids,
                           'total_carbohydrates': total_carbohydrates})
        except Exception as e:
            return render(request, 'home/home.html')
    else:
        return render(request, 'home/home.html')
