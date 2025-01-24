from .models import NewsletterRequest
from django import forms


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterRequest
        fields = ('name', 'email')
