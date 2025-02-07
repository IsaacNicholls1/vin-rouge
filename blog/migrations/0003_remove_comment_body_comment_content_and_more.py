# Generated by Django 4.2.17 on 2025-02-07 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_comment_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='body',
        ),
        migrations.AddField(
            model_name='comment',
            name='content',
            field=models.TextField(default='Leave your review here'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, unique=True),
        ),
    ]
