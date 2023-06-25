from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta :
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        labels = {
            'email' : _('email')
        }

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta :
        model = User
        fields = ['username', 'email']

        labels = {
            'email' : _('email'),
            'image' : _('image'),
        }

class ProfileUpdateForm(forms.ModelForm): 
    class Meta : 
        model = Profile
        fields = ['image', 'language']

        labels = {
            'image' : _('image'),
            'language' : _('language')
        }