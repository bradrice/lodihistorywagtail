"""Standard page."""
from django.db import models

from wagtail.admin.panels import FieldPanel 
from wagtail.models import Page
from wagtail.fields import StreamField
from streams import blocks


class StandardPage(Page):
    """Standard page class."""

    template = "standard/standard_page.html"

    # @todo add streamfields 
    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("simple_richtext", blocks.RichtextBlock()),
        ],
        null=True,
        blank=True,
        use_json_field=True
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
        FieldPanel("page_image"),
        FieldPanel("content"),
    ]

    class Meta:  # noqa 
        verbose_name = "Standard Page"
        verbose_name_plural = "Standard Pages"
