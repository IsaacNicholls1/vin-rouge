# Generated by Django 4.2.17 on 2025-02-06 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_winereviewsubmission_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('subject', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
