"""
Import from django and from models module
"""
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Create class to generate form for Comments.
    """
    class Meta:
        model = Comment
        fields = ('name', 'body',)
