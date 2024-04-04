from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('profile/', include('user_profile.urls')),
    path('products/', include('product.urls')),
]
