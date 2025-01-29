from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))

"""
Review model - to store wine reviews
"""
class Review(models.Model):
    REGION_CHOICES = [
        ('southwest', 'Southwest'),
        ('northwest', 'Northwest'),
        ('northeast', 'Northeast'),
        ('southeast', 'Southeast'),
        ('central', 'Central'),
    ]

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="review_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    region = models.CharField(max_length=200, choices=REGION_CHOICES, default='southwest')
    status = models.IntegerField(choices=STATUS, default=0)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments_author",
        default=1
    )
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment by {self.author.username}'

class Region(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="region_posts")
    name = models.CharField(max_length=100)
    featured_image = CloudinaryField('image', default='redwine')
    slug = models.SlugField(max_length=100, unique=True)
    created = models.DateTimeField(auto_now_add=True)


class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
