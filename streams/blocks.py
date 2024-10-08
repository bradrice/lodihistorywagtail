# streams/blocks.py
from wagtail import blocks
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock


class TitleAndTextBlock(blocks.StructBlock):
    """Title and text and nothing else."""

    title = blocks.CharBlock(required=True, help_text="Add your title")
    text = blocks.RichTextBlock(required=True, help_text="Add additional text", features=['bold', 'italic', 'link'])

    class Meta:  # noqa
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"

class RichtextBlock(blocks.RichTextBlock):
    """Richtext with all the features."""

    class Meta:  # noqa
        template = "streams/richtext_block.html"
        icon = "doc-full"
        label = "Full RichText"


class SimpleRichtextBlock(blocks.RichTextBlock):
    """Richtext without (limited) all the features."""

    def __init__(
        self, required=True, help_text=None, editor="default", features=None, **kwargs
    ):  # noqa
        super().__init__(**kwargs)
        self.features = ["bold", "italic", "link", "h1", "h2", "h3", "h4", "h5", "p", "ul", "ol", "hr", "br", "media"]

    class Meta:  # noqa
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "Simple RichText"


class DocBlock(blocks.StreamBlock):
    """Document chooser"""
    
    title = blocks.CharBlock(required=True, help_text="Add your title")
    # doc = DocumentChooserBlock(required=True)
    # link = blocks.CharBlock(required=True, help_text="Add your title")

    class Meta:  # noqa
        # template = "streams/title_and_link_block.html"
        icon = "edit"
        label = "Document Link"


class PhotoCategoryBlock(blocks.StructBlock):

    heading = blocks.CharBlock(form_classname="full title")
    paragraph = blocks.RichTextBlock()
    image = ImageChooserBlock(required=False)
    category = SnippetChooserBlock('photos.PhotoCategory', max_count=1)

    class Meta:  # noqa
        template = "streams/photo_category_block.html"
        icon = "edit"
        label = "Photo category block"