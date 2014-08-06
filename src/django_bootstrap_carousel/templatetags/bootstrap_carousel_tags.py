# -*- coding: utf-8 -*-

from django import template


registry = template.Library()


@registry.simple_tag(takes_context=True, template='django_bootstrap_carousel/carousel.html')
def render_carousel(context, carousel):
    context.update({
        'carousel': carousel,
    })
    return context

