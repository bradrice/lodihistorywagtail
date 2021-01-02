from django.db import models
from django.shortcuts import render
from django import forms
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from streams import blocks
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel
from wagtail.images.models import Image, AbstractImage, AbstractRendition
from wagtail.images.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalKey
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.contrib.routable_page.models import route, RoutablePageMixin


@register_snippet
class PhotoCategory(models.Model):
    """Blog category for a snippet."""

    name = models.CharField(max_length=255)
    slug = models.SlugField(
        verbose_name="slug",
        allow_unicode=True,
        max_length=255,
        help_text='A slug to identify photos by this category',
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("slug"),
    ]

    class Meta:
        verbose_name = "Photo Category"
        verbose_name_plural = "Photo Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Photo(AbstractImage):
    # Add any extra fields to image here

    # eg. To add a caption field:
    caption = models.CharField(max_length=255, blank=True)
    category = models.ManyToManyField(PhotoCategory, blank=True, related_name="categories")

    admin_form_fields = Image.admin_form_fields + (
        # Then add the field names here to make them appear in the form:
        'caption',
        "category",
    )


class CustomRendition(AbstractRendition):
    image = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='renditions')

    class Meta:
        unique_together = (
            ('image', 'filter_spec', 'focal_point_key'),
        )

class PhotosListingPage(RoutablePageMixin, Page):
    """Phostos listing page"""

    template = "photos/photos_list_page.html"

    subtitle = models.CharField(max_length=100, null=True, blank=True)
    body = StreamField(
        [
        ('photo_category', blocks.PhotoCategoryBlock())
        ], null=True, blank=True
        )

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        StreamFieldPanel("body")
    ]

    @route(r"^collection/(?P<cat_slug>[-\w]*)/$", name="category_view")
    def collection_view(self, request, cat_slug):
        """Find blog posts based on a category."""
        context = self.get_context(request)
        print(cat_slug)
        

        try:
            # Look for the blog category by its slug.
            category = PhotoCategory.objects.get(slug=cat_slug)
            print(category.id)
        except Exception:
            # Blog category doesnt exist (ie /blog/category/missing-category/)
            # Redirect to self.url, return a 404.. that's up to you!
            category = None

        if category is None:
            # This is an additional check.
            # If the category is None, do something. Maybe default to a particular category.
            # Or redirect the user to /blog/ ¯\_(ツ)_/¯
            pass

        photos = Photo.objects.filter(category=category.id)
        context["photos"] = photos
        for photo in photos:
            print(photo.title)
        # Note: The below template (latest_posts.html) will need to be adjusted
        return render(request, "photos/photos_page.html", context)