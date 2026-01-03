from django.contrib import admin
from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    """
    Job admin interface.
    Follows Single Responsibility Principle.
    """
    list_display = ['title', 'company_name', 'location', 'job_type', 'is_active', 'posted_date']
    list_filter = ['is_active', 'job_type', 'posted_date']
    search_fields = ['title', 'company_name', 'location', 'description']
    readonly_fields = ['slug', 'posted_date', 'updated_date']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'company_name', 'location', 'job_type')
        }),
        ('Details', {
            'fields': ('description', 'requirements', 'responsibilities', 'salary_range')
        }),
        ('Status', {
            'fields': ('is_active', 'slug')
        }),
        ('Timestamps', {
            'fields': ('posted_date', 'updated_date'),
            'classes': ('collapse',)
        }),
    )
