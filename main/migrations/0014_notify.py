# Generated by Django 3.2.5 on 2024-03-14 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0013_auto_20240314_1605'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notify',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notify_detail', models.TextField()),
                ('read_by_trainer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.trainer')),
                ('read_by_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
