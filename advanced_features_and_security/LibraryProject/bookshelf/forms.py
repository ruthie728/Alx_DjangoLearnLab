from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']


# Add this to fix the test
class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()