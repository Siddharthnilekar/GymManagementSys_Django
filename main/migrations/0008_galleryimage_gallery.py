# Generated by Django 5.0 on 2024-03-08 08:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_gallery_galleryimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryimage',
            name='gallery',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.gallery'),
        ),
    ]