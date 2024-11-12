# Generated by Django 4.1 on 2024-08-26 20:16

from django.db import migrations, models
import wagtail.images.models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0013_auto_20220430_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customrendition',
            name='file',
            field=wagtail.images.models.WagtailImageField(height_field='height', upload_to=wagtail.images.models.get_rendition_upload_to, width_field='width'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=wagtail.images.models.WagtailImageField(height_field='height', upload_to=wagtail.images.models.get_upload_to, verbose_name='file', width_field='width'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='file_hash',
            field=models.CharField(blank=True, db_index=True, editable=False, max_length=40),
        ),
    ]