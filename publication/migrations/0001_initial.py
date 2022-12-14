# Generated by Django 4.1.1 on 2022-10-04 01:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_name', models.CharField(max_length=30)),
                ('food_type', models.TextField(max_length=3000)),
                ('rest_pic', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer', models.CharField(default='anonymous', max_length=40)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('stars', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('detail', models.TextField(default='Type here your review.', max_length=4000)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publication.restaurant')),
            ],
        ),
    ]
