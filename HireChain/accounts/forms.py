from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class UserRegisterForm(UserCreationForm):
    """
    User registration form.
    Follows Open/Closed Principle - extends UserCreationForm without modifying it.
    """
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-input',
        'placeholder': 'Email Address'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input',
        'placeholder': 'Username'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-input',
        'placeholder': 'Password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-input',
        'placeholder': 'Confirm Password'
    }))
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    """
    User login form.
    Follows Open/Closed Principle - extends AuthenticationForm.
    """
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input',
        'placeholder': 'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-input',
        'placeholder': 'Password'
    }))
