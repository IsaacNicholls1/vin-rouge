from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Wine, Review, Comment

class ReviewAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'wine', 'status',)
    search_fields = ['title',]
    list_filter = ('status', 'created_on', 'wine',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(Comment)
admin.site.register(Wine)
admin.site.register(Review, ReviewAdmin)





