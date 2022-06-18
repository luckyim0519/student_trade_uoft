from django import forms
from .models import signupModel

class FormSignupForm(forms.ModelForm):
    class Meta:
        model = signupModel
        fields=["username","email","password"]