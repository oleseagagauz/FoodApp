from django.urls import path
from . import views

app_name = 'user_profile'

urlpatterns = [
    path('', views.view_profile, name='view_profile'),
    path('fill/', views.fill_profile, name='fill_profile'),
    path('edit/', views.edit_profile, name='edit_profile'),
    path('imt/', views.imt, name='imt'),

]
