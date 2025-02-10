from django import forms
from .models import WineReview


class WineReviewForm(forms.ModelForm):
    class Meta:
        model = WineReview
        fields = ('content', 'title', 'rating', 'featured_image')
