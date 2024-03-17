from django import forms
from django.contrib.auth.models import User

class SignupForm(forms.Form):
    username=forms.CharField(max_length=255)
    email=forms.EmailField()
    password=forms.CharField(max_length=255)
    password2=forms.CharField(max_length=255)


class LoginForm(forms.Form):
    username=forms.CharField(max_length=255)
    password=forms.CharField(max_length=255)

class UserEdit(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email']

class DeleteForm(forms.ModelForm):
    class Meta:
        model=User
        fields=[]