# Generated by Django 5.0.6 on 2025-04-08 15:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quora', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='disliked_answers', to=settings.AUTH_USER_MODEL),
        ),
    ]
