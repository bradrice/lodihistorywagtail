# Generated by Django 3.1.4 on 2021-01-01 21:03

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0007_auto_20210101_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photoslistingpage',
            name='body',
            field=wagtail.fields.StreamField([('photo_category', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(form_classname='full title')), ('paragraph', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('category', wagtail.snippets.blocks.SnippetChooserBlock('photos.PhotoCategory', max_count=1))]))], blank=True, null=True),
        ),
    ]
