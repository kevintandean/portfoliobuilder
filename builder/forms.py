# from django.contrib.auth import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from builder.models import Project

__author__ = 'kevin'

class ProjectImageForm(ModelForm):
    class Meta:
        model = Project
        fields = ['image']

# Should name this something other than Form
class Form(UserCreationForm):
    username = forms.RegexField(label=("Username"), max_length=30,
        regex=r'^[\w.@+-]+$',
        help_text=(""),
        error_messages={
            'invalid': ("This value may contain only letters, numbers and "
                         "@/./+/-/ characters.")},
        widget=forms.TextInput(attrs={'placeholder': 'username', 'class': 'form-control'}))

    password1 = forms.CharField(label=("Password"),
        widget=forms.PasswordInput(attrs={'placeholder': 'password', 'class': 'form-control'}))

    password2 = forms.CharField(label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={'placeholder': 'verify password', 'class': 'form-control'}),
        help_text=(""))
