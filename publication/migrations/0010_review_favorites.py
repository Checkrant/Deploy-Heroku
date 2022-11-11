# Generated by Django 4.1 on 2022-10-26 12:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('publication', '0009_remove_review_user_favorites'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='favorites',
            field=models.ManyToManyField(related_name='favorites', to=settings.AUTH_USER_MODEL),
        ),
    ]