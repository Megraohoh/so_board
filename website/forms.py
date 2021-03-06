from django.contrib.auth.models import User
from django import forms
from website.models import *

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
        

class GameForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = ('name', 'description', 'image', 'user')

