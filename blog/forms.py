from django import forms
from .models import Review, Comment

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'author', 'featured_image', 'wine', 'content', 'rating']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', 'title', 'rating',) 









