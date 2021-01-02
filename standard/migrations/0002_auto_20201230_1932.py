# Generated by Django 3.1.4 on 2020-12-30 19:32

from django.db import migrations
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standardpage',
            name='content',
            field=wagtail.core.fields.StreamField([('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link'], help_text='Add additional text', required=True))])), ('simple_richtext', streams.blocks.RichtextBlock())], blank=True, null=True),
        ),
    ]
