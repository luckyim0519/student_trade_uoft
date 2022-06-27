from django import forms
from .models import BookBoardModel


class BookBoardForm(forms.ModelForm):
    class Meta:
        model = BookBoardModel
        fields =['title', 'content', 'writer']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'writer': forms.TextInput(attrs={'class': 'form-control'})
        }
