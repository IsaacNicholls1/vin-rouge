# Generated by Django 4.2.17 on 2025-02-03 21:48

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('name', models.CharField(default='wine-name', max_length=100, unique=True)),
                ('maker', models.CharField(max_length=100)),
                ('region', models.CharField(choices=[('Bordeaux', 'Bordeaux'), ('Burgundy', 'Burgundy'), ('Rhône Valley', 'Rhône Valley'), ('Loire Valley', 'Loire Valley'), ('Languedoc-Roussillon', 'Languedoc-Roussillon'), ('Beaujolais', 'Beaujolais'), ('Alsace', 'Alsace'), ('Other', 'Other')], max_length=100)),
                ('vintage', models.IntegerField()),
                ('grape', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('featured_image', cloudinary.models.CloudinaryField(default='redwine', max_length=255, verbose_name='image')),
                ('excerpt', models.TextField(default='wine-name', max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wines', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('content', models.TextField()),
                ('rating', models.IntegerField(choices=[(1, '1🍷'), (2, '2🍷'), (3, '3🍷'), (4, '4🍷'), (5, '5🍷')], default=None)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_posts', to=settings.AUTH_USER_MODEL)),
                ('wine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewed_wine', to='blog.wine')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('title', models.CharField(default='Default Title', max_length=200)),
                ('body', models.TextField()),
                ('approved', models.BooleanField(default=False)),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('rating', models.IntegerField(choices=[(1, '1🍷'), (2, '2🍷'), (3, '3🍷'), (4, '4🍷'), (5, '5🍷')], default=None)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_author', to=settings.AUTH_USER_MODEL)),
                ('wine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_wine', to='blog.wine')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
