from allauth.account.forms import LoginForm
from django import forms
from .models import CustomUser


class CustomLoginForm(LoginForm):
    age = forms.IntegerField(label='Age', required=False)
    country = forms.CharField(max_length=100, label='Country', required=False)

    def custom_signup(self, request, user):
        user.age = self.cleaned_data.get('age', None)
        user.country = self.cleaned_data.get('country', '')
        user.save()
