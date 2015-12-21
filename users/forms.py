from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from myblog import settings
from users.models import Profile

GENDER = (
    ('F', 'Female'),
    ('M', 'Male')
)

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label="Repeat password")

class LoginForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class EditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["gender", "about_me", "avatar"]

    avatar = forms.ImageField(required=False)