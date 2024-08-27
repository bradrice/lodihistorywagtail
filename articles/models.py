from django.db import models
from wagtail.models import Collection
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from streams import blocks
from wagtail.admin.panels import FieldPanel, PageChooserPanel 
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
        use_json_field=True
    )

    subtitle = models.CharField(max_length=100, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        FieldPanel("content"),

    ]

    class Meta: 
        verbose_name = "Article Page"
        verbose_name_plural = "Article Pages"

    @route(r"^$", name="collection_view")
    def collection_view(self, request):

        """Find blog posts based on a category."""
        context = super().get_context(request)
        # context = self.get_context(request)

        collection_id = Collection.objects.get(name='articles').id
        context['documents'] = Document.objects.filter(collection=collection_id)
        print(context['documents'][0].collection)
        return render(request, "article/article_page.html", context)

    
