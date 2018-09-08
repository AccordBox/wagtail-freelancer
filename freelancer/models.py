from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import six
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from wagtail.admin.edit_handlers import (FieldPanel, FieldRowPanel,
                                         InlinePanel, MultiFieldPanel,
                                         StreamFieldPanel)
from wagtail.contrib.forms.models import AbstractForm, AbstractFormField
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page, PageBase
from wagtail.images.edit_handlers import ImageChooserPanel

from freelancer.blocks import PortfolioBlock
from modelcluster.fields import ParentalKey


class FreelancerFormField(AbstractFormField):
    page = ParentalKey('FreelancerPage', related_name='form_fields')


class FreelancerPage(AbstractForm):
    subtitle = models.CharField(max_length=100, blank=True)
    profile_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    portfolio = StreamField([
        ('portfolio', PortfolioBlock()),
    ], null=True, blank=True)

    about_text = RichTextField(blank=True)
    about_CTA_text = models.CharField(max_length=100, blank=True)
    about_CTA_link = models.URLField(blank=True)

    content_panels = AbstractForm.content_panels + [
        MultiFieldPanel([
            FieldPanel('subtitle'),
            ImageChooserPanel('profile_image'),
        ], "Hero"),

        StreamFieldPanel('portfolio'),

        MultiFieldPanel([
            FieldPanel('about_text', classname="full"),
            FieldPanel('about_CTA_text'),
            FieldPanel('about_CTA_link'),
        ], "Hero"),

        InlinePanel('form_fields', label="Form fields"),

    ]
