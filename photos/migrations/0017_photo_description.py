# Generated by Django 5.1.3 on 2024-11-12 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0016_alter_customrendition_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='description',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='description'),
        ),
    ]
