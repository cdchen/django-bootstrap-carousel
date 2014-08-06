# -*- coding: utf-8 -*-

from django import template


register = template.Library()


@register.inclusion_tag('django_bootstrap_carousel/carousel.html', takes_context=True)
def render_carousel(context, carousel, carousel_id=None):
    carousel_id = carousel_id or 'carousel-%d' % carousel.pk
    context.update({
        'carousel': carousel,
        'carousel_id': carousel_id,
    })
    return context

