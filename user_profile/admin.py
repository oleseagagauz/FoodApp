from django.contrib import admin
from .models import UserProfile, UserIMT


# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'sex', 'scope', 'activity_level', 'weight', 'height', 'birthdate', 'creation_date']
    list_filter = ['scope', 'activity_level']
    search_fields = ['user__username', 'user__email']  # Поиск по имени пользователя или электронной почте


@admin.register(UserIMT)
class UserIMTAdmin(admin.ModelAdmin):
    list_display = ['user', 'value', 'status']
    list_filter = ['value', 'status']
    search_fields = ['user__username', 'user__email']