"""Standard page."""
from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from streams import blocks
from wagtail.images.edit_handlers import ImageChooserPanel


class StandardPage(Page):
    """Standard page class."""

    template = "standard/standard_page.html"

    # @todo add streamfields 
    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("simple_richtext", blocks.SimpleRichtextBlock()),
        ],
        null=True,
        blank=True,
    )
    page_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    subtitle = models.CharField(max_length=100, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        ImageChooserPanel("page_image"),
        StreamFieldPanel("content"),
    ]

    class Meta:  # noqa 
        verbose_name = "Standard Page"
        verbose_name_plural = "Standard Pages"