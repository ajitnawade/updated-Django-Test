from django import forms
from .models import Client,Project

class LoginAdmin(forms.Form):
    email =forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())


class ClientForm(forms.ModelForm):
    class Meta():
        model = Client
        fields= ('client_name',)
        # exclude=[]




class LoginUser(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())