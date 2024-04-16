from allauth.account.forms import SignupForm, LoginForm
from django import forms
from .models import CustomUser


class CustomLoginForm(LoginForm):
    first_name = forms.CharField(max_length=100, label='First Name')
    last_name = forms.CharField(max_length=100, label='Last Name', required=False)
    age = forms.IntegerField(label='Age', required=False)
    country = forms.CharField(max_length=100, label='Country', required=False)

    def custom_signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data.get('last_name', '')
        user.age = self.cleaned_data.get('age', None)
        user.country = self.cleaned_data.get('country', '')
        user.save()
