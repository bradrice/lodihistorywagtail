# Generated by Django 3.2.13 on 2022-04-30 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nav', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
