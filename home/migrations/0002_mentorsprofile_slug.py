# Generated by Django 4.1.7 on 2023-03-19 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentorsprofile',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
