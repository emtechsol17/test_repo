from django import forms
from django.contrib.auth.models import User
from loginapp.models import UserProfileInfo


class UserForm(forms.ModelForm):

    password = forms.CharField(widget = forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','password','email')

class UserProfileInfoform(forms.ModelForm):

    class Meta():
        model =  UserProfileInfo
        fields = ('profile_pic',)
