# Generated by Django 4.2.17 on 2025-01-29 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_review_region'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='excerpt',
        ),
    ]
