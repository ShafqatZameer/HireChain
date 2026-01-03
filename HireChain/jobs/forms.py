from django import forms
from .models import Job


class JobForm(forms.ModelForm):
    """
    Job posting form for admins.
    Follows Single Responsibility Principle - handles job creation.
    """
    class Meta:
        model = Job
        fields = ['title', 'company_name', 'location', 'description', 'requirements', 
                  'responsibilities', 'salary_range', 'job_type', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Job Title'
            }),
            'company_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Company Name'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Location (e.g., New York, NY)'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Job Description',
                'rows': 5
            }),
            'requirements': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Requirements (Optional)',
                'rows': 4
            }),
            'responsibilities': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Responsibilities (Optional)',
                'rows': 4
            }),
            'salary_range': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Salary Range (Optional)'
            }),
            'job_type': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Job Type (e.g., Full-time, Part-time)'
            }),
        }
