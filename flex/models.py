from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, PageChooserPanel 
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
        use_json_field=True
    )

    subtitle = models.CharField(max_length=100, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        FieldPanel("content"),

    ]

    class Meta: 
        verbose_name = "Flex Page"
        verbose_name_plural = "Flex Pages"
