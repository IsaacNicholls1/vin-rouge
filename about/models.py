from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

"""
About model - to store information about the site owner
"""
class About(models.Model):
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    profile_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.title


class NewsletterRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Newletter request from {self.name}"