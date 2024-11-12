# Generated by Django 4.1 on 2024-08-26 20:40

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0014_alter_customrendition_file_alter_photo_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photoslistingpage',
            name='body',
            field=wagtail.fields.StreamField([('photo_category', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(form_classname='full title')), ('paragraph', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('category', wagtail.snippets.blocks.SnippetChooserBlock('photos.PhotoCategory', max_count=1))]))], blank=True, null=True, use_json_field=True),
        ),
    ]