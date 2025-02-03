# Generated by Django 4.2.17 on 2025-02-03 14:38

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_wine_excerpt'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.IntegerField(choices=[(1, '1🍷'), (2, '2🍷'), (3, '3🍷'), (4, '4🍷'), (5, '5🍷')], default=None),
        ),
        migrations.AddField(
            model_name='comment',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
