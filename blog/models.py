from django.db import models
import uuid
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify

STATUS = ((0, "Draft"), (1, "Published"))
RATING = ((1, "1🍷"), (2, "2🍷"), (3, "3🍷"), (4, "4🍷"), (5, "5🍷"))

# Wine model 
class Wine(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    name = models.CharField(max_length=100, unique=True, default="wine-name")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="wines"
    )
    maker = models.CharField(max_length=100)
    REGION_CHOICES = (
        ('Bordeaux', 'Bordeaux'),
        ('Burgundy', 'Burgundy'),
        ('Rhône Valley', 'Rhône Valley'),
        ('Loire Valley', 'Loire Valley'),
        ('Languedoc-Roussillon', 'Languedoc-Roussillon'),
        ('Beaujolais', 'Beaujolais'),
        ('Alsace', 'Alsace'),
        ('Other', 'Other'),
    )
    region = models.CharField(max_length=100, choices=REGION_CHOICES)
    vintage = models.IntegerField()
    grape = models.CharField(max_length=100)
    description = models.TextField()
    featured_image = CloudinaryField('image', default='redwine')
    excerpt = models.TextField(max_length=100, default="wine-name")

    class Meta:
        ordering = ["-title"]

    def __str__(self):
        return self.name

# wine review model for users to submit reviews
class WineReview(models.Model):
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    title = models.CharField(max_length=200, default="Default Title")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments_author"
    )
    wine = models.ForeignKey(
        Wine, on_delete=models.CASCADE, related_name="comments_wine"
    )
    approved = models.BooleanField(default=False)
    featured_image = CloudinaryField(
        'image', default='pexels-brettjordan-18687127_v6rpui'
    )
    status = models.IntegerField(choices=STATUS, default=0)
    content = models.TextField(default="Leave your review here")
    rating = models.IntegerField(choices=RATING, default=None)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return (
            f'Wine Review by {self.author.username}. '
            f'This wine - {self.wine} gets {self.rating}/5'
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title + "-" + str(uuid.uuid4()))
        super().save(*args, **kwargs)


class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
