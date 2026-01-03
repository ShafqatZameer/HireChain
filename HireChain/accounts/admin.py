from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """
    Custom user admin interface.
    Follows Open/Closed Principle - extends UserAdmin.
    """
    list_display = ['username', 'email', 'user_type', 'is_active', 'date_joined']
    list_filter = ['user_type', 'is_active', 'is_staff']
    search_fields = ['username', 'email', 'phone']
    
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('user_type', 'phone', 'linkedin')}),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('user_type', 'email', 'phone', 'linkedin')}),
    )
