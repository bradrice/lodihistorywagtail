# Generated by Django 3.1.4 on 2021-01-03 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0010_auto_20210101_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='categories', to='photos.PhotoCategory'),
        ),
    ]
