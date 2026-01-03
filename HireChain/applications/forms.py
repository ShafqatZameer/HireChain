from django import forms
from .models import Application


class ApplicationForm(forms.ModelForm):
    """
    Job application form.
    Follows Single Responsibility Principle - handles application submission.
    """
    class Meta:
        model = Application
        fields = ['full_name', 'email', 'phone', 'linkedin', 'resume', 'portfolio', 'cover_letter']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Full Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'Email Address'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Phone Number'
            }),
            'linkedin': forms.URLInput(attrs={
                'class': 'form-input',
                'placeholder': 'LinkedIn Profile URL (Optional)'
            }),
            'portfolio': forms.URLInput(attrs={
                'class': 'form-input',
                'placeholder': 'Portfolio URL (Optional)'
            }),
            'cover_letter': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Cover Letter',
                'rows': 5
            }),
            'resume': forms.FileInput(attrs={
                'class': 'form-file-input',
                'accept': '.pdf,.doc,.docx'
            })
        }
