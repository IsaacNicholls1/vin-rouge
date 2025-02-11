from django.db import models
from cloudinary.models import CloudinaryField

# Create models here.

"""
About model - to store information about the site owner

"""


class About(models.Model):
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(default="This is the about page content")
    profile_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.title

# NewsletterRequest model - to store newsletter requests

class NewsletterRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Newletter request from {self.name}"

# WineReviewSubmission model - to store wine reviews

class WineReviewSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    wine_name = models.CharField(max_length=100)
    review = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    submitted_on = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return f"Review by {self.name} for {self.wine_name}"

# Newsletter model - to store newsletters in the admin panel 

class Newsletter(models.Model):
    subject = models.CharField(max_length=200)
    pdf_file = models.FileField(
        upload_to='newsletters/',
        default='path/to/default.pdf'
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject
