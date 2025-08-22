from django import forms
from .models import Post, Comment

# Form to create or edit a blog post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']  # slug is auto-generated, author set in view
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter post title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your content here...', 'rows': 6}),
        }

# Form to add a comment on a post
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Add a comment...', 'rows': 3}),
        }
