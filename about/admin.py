from django.contrib import admin
from .models import About, NewsletterRequest, WineReviewSubmission
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


@admin.register(NewsletterRequest)
class NewsletterRequestAdmin(admin.ModelAdmin):
    list_display = ('read', 'name', 'email')


@admin.register(WineReviewSubmission)
class WineReviewSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'wine_name', 'rating', 'submitted_on', 'image', 'email', 'review')
    search_fields = ['name', 'wine_name']
    list_filter = ('submitted_on',)