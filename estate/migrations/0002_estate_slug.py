# Generated by Django 3.2.7 on 2021-09-09 17:48

from django.db import migrations, models
import estate.models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estate',
            name='slug',
            field=models.SlugField(default=estate.models.generate_slug, editable=False, unique=True, verbose_name='Slug'),
        ),
    ]
