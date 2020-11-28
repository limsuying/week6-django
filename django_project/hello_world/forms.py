from django import forms
from hello_world.models import UserProfileInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
        # widgets = {
        #     'username': forms.TextInput(attrs={'class':'form-control','style':'color:red'}),
        #     'password': forms.PasswordInput(attrs={'class':'form-control'}),
        #     'email':forms.TextInput(attrs={'class':'form-control'})
        # }

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('occupation','company','hobby')