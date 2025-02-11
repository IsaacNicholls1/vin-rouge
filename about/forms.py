from .models import NewsletterRequest, WineReviewSubmission
from django import forms

# Create a form for newsletter request

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterRequest
        fields = ('name', 'email')

# Create a form for wine review submission

class WineReviewSubmissionForm(forms.ModelForm):
    class Meta:
        model = WineReviewSubmission
        fields = ['name', 'email', 'wine_name', 'review', 'rating', 'image',]
