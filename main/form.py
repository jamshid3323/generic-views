from django import forms
from .models import BooksModel


class CreateBookForm(forms.ModelForm):

    class Meta:
        model = BooksModel
        fields = ['name', 'price']

