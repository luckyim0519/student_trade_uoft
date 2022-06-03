from django import forms
from .models import signupForm

class FormSignupForm(forms.ModelForm):
    class Meta:
        model = signupForm
        fields=["username","email","password"]