# Generated by Django 5.1.2 on 2024-11-07 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='content_images/'),
        ),
    ]
