from .models import NewsletterRequest, WineReviewSubmission
from django import forms


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterRequest
        fields = ('name', 'email')


class WineReviewSubmissionForm(forms.ModelForm):
    class Meta:
        model = WineReviewSubmission
        fields = ['name', 'email', 'wine_name', 'review', 'rating']
