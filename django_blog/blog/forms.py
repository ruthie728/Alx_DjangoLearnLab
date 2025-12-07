# blog/forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    """
    ModelForm for creating and updating Post objects.
    'author' is not exposed on the form and will be set
    automatically in the CreateView / UpdateView.
    """
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Post title', 'class': 'form-input'}),
            'content': forms.Textarea(attrs={'placeholder': 'Write your post here...', 'class': 'form-textarea', 'rows': 10}),
        }