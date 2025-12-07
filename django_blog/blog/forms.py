from django import forms
from .models import Post, Comment
from taggit.forms import TagWidget  # Import TagWidget for tagging


# ---------------------------
# Post Form
# ---------------------------
class PostForm(forms.ModelForm):
    """
    ModelForm for creating and updating Post objects.
    'author' is not exposed on the form and will be set
    automatically in the CreateView / UpdateView.
    """
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Include tags
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Post title', 'class': 'form-input'}),
            'content': forms.Textarea(attrs={'placeholder': 'Write your post here...', 'class': 'form-textarea', 'rows': 10}),
            'tags': TagWidget(),  # <-- exactly TagWidget() for the check
        }

    # Optional: Custom validation
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long.")
        return title

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 20:
            raise forms.ValidationError("Content must be at least 20 characters long.")
        return content


# ---------------------------
# Comment Form
# ---------------------------
class CommentForm(forms.ModelForm):
    """
    ModelForm for creating and updating Comment objects.
    'author' and 'post' are set automatically in the view.
    """
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Write a comment...', 'class': 'form-textarea', 'rows': 4}),
        }

    # Optional: Custom validation
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 2:
            raise forms.ValidationError("Comment must be at least 2 characters long.")
        return content