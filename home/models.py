from django.db import models

from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page

from wagtail.blocks import RichTextBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock

class HomePage(Page):
    # поле в БД
    subtitle = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Підзаголовок"
    )
    rtfbody = RichTextField(
         blank=True,
         null=True,
    )
    body = StreamField([
        ("rtfblock", RichTextBlock()),
        ("imgblock", ImageChooserBlock()),
        ("videoblock", EmbedBlock())
    ],
        blank=True
    )
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Homepage image"
    )


    # поле для ввода в Админке
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
            FieldPanel("subtitle"),
            FieldPanel("rtfbody"),
            ], heading="Main content"
        ),
        FieldPanel("image"),
        FieldPanel("body")
    ]
    # promote_panels = []
    # setting_panels = []
