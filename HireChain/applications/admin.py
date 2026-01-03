from django.contrib import admin
from .models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    """
    Application admin interface.
    Follows Single Responsibility Principle.
    """
    list_display = ['full_name', 'job', 'email', 'status', 'applied_date']
    list_filter = ['status', 'applied_date']
    search_fields = ['full_name', 'email', 'phone', 'job__title']
    readonly_fields = ['applied_date', 'updated_date']
    
    fieldsets = (
        ('Applicant Information', {
            'fields': ('user', 'full_name', 'email', 'phone', 'linkedin')
        }),
        ('Job Application', {
            'fields': ('job', 'status')
        }),
        ('Documents', {
            'fields': ('resume', 'portfolio', 'cover_letter')
        }),
        ('Timestamps', {
            'fields': ('applied_date', 'updated_date'),
            'classes': ('collapse',)
        }),
    )
    
    def get_readonly_fields(self, request, obj=None):
        """Make user and job readonly after creation"""
        if obj:
            return self.readonly_fields + ['user', 'job']
        return self.readonly_fields
