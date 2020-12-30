from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from streams import blocks
from wagtail.documents.blocks import DocumentChooserBlock

class FlexPage(Page):
    """Flexible page class."""

    template = "flex/flex_page.html"

    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("full_richtext", blocks.RichtextBlock()),
            ("docLink", DocumentChooserBlock(required=True, template="streams/title_and_link_block.html"))
        ],
        null=True,
        blank=True,
    )

    subtitle = models.CharField(max_length=100, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        StreamFieldPanel("content"),

    ]

    class Meta: 
        verbose_name = "Flex Page"
        verbose_name_plural = "Flex Pages"