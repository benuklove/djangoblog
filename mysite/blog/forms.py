from django import forms
from .models import Comment

# Skipping the feature: share post via email form

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
