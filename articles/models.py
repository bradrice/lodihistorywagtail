from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from streams import blocks
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel
from wagtail.documents.models import Document
from django.shortcuts import render, redirect
from wagtail.contrib.routable_page.models import route, RoutablePageMixin


# Create your models here.

class ArticleListingPage(RoutablePageMixin, Page):
    """Article listing page"""

    template = "article/article_page.html"

    content = StreamField(
        [
            ("full_richtext", blocks.RichtextBlock()),
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
        verbose_name = "Article Page"
        verbose_name_plural = "Article Pages"

    @route(r"^$", name="collection_view")
    def collection_view(self, request):
        """Find blog posts based on a category."""
        context = self.get_context(request)

        context['documents'] = Document.objects.all()
        print(context)
        return render(request, "article/article_page.html", context)

    