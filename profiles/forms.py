from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ['email','first_name','last_name','username','biography','is_public']


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = Profile
        fields = ['email','first_name','last_name','username','biography','is_public']

