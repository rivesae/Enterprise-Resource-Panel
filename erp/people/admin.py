from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserInfo
from core.models import CustomUser

class ProfileInline(admin.StackedInline):
    model = UserInfo

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    inlines = [ProfileInline]
    list_display = ['email', 'first_name', 'last_name', 'is_staff']  # Add other fields you want to display
    ordering = ['email']  # Use 'email' instead of 'username' for ordering
    
admin.site.unregister(CustomUser)
admin.site.register(CustomUser, CustomUserAdmin)