from wagtail.admin.edit_handlers import (FieldPanel, FieldRowPanel,
                                         InlinePanel, MultiFieldPanel,
                                         PageChooserPanel, StreamFieldPanel)
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock


class PortfolioBlock(blocks.StructBlock):
    heading = blocks.CharBlock(classname="full title")
    image = ImageChooserBlock()
    intro = blocks.RichTextBlock()

    class Meta:
        template = 'freelancer/blocks/portfolio.html'
