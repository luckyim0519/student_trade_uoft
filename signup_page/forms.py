from django import forms
from django.contrib.auth import get_user_model
from .models import signupModel

class FormSignupForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = signupModel
        fields=["username","email","password"]