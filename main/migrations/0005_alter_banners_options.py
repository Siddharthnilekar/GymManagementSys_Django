# Generated by Django 5.1.3 on 2025-01-10 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_alter_banners_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="banners",
            options={"verbose_name_plural": "Banners"},
        ),
    ]
