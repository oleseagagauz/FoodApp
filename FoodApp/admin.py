from django.contrib import admin


class CustomAdminSite(admin.AdminSite):
    site_title = 'My'
    site_icon = 'static/favicon/favicon.png'
