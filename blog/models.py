from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

class Region(models.Model):
    REGION_CHOICES = [
        ('southwest', 'Southwest'),
        ('northwest', 'Northwest'),
        ('northeast', 'Northeast'),
        ('southeast', 'Southeast'),
        ('central', 'Central'),
    ]
    
    name = models.CharField(max_length=100, choices=REGION_CHOICES)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Wine(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="region_posts")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wines")
    maker = models.CharField(max_length=100)
    vintage = models.IntegerField()
    grape = models.CharField(max_length=100)
    description = models.TextField()
    featured_image = CloudinaryField('image', default='redwine')
    slug = models.SlugField(unique=True, default='default-slug')

    def __str__(self):
        return self.name

class Review(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="review_posts")
    featured_image = CloudinaryField('image', default='placeholder')
    wine = models.ForeignKey(Wine, on_delete=models.CASCADE, related_name="reviewed_wine")
    status = models.IntegerField(choices=STATUS, default=0)
    content = models.TextField()
    rating = models.IntegerField(default=0, choices=[(i, i) for i in range(1, 6)])
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]
    
    def __str__(self):
        return f'{self.wine} - {self.rating}/5'

class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments_author")
    wine = models.ForeignKey(Wine, on_delete=models.CASCADE, related_name="comments_wine")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment by {self.author.username}'

class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title