from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta: #when form is accepted it create a new user
        model = User
        fields= ['username' , 'email', 'password1', 'password2']
