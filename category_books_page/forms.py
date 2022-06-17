from django import forms
from .models import BookBoardModel

class BookBoardForm(forms.ModelForm):
    class Meta:
        model = BookBoardModel
        fields =['title', 'content', 'writer']