from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    """Admin view for user class"""
    list_display = ['username', 'email', 'password', 'is_staff', 'created_at', 'is_verified']


admin.site.register(User, UserAdmin)
