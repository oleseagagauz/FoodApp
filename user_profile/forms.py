from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['sex', 'scope', 'activity_level', 'weight', 'height', 'birthdate']
        labels = {
            'sex': 'Пол',
            'scope': 'Цель',
            'activity_level': 'Уровень активности',
            'weight': 'Вес (кг)',
            'height': 'Рост (см)',
            'birthdate': 'Дата рождения',
        }
        widgets = {
            'birthdate': forms.DateInput(attrs={'type': 'date'})
        }


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['sex', 'scope', 'activity_level', 'weight', 'height']
        labels = {
            'sex': 'Пол',
            'scope': 'Цель',
            'activity_level': 'Уровень активности',
            'weight': 'Вес (кг)',
            'height': 'Рост (см)',
        }
