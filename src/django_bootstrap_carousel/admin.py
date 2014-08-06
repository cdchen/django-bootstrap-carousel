# -*- coding: utf-8 -*-
#
# django-bootstrap-carousel
#
from django.contrib import admin
from django_bootstrap_carousel.models import Carousel, CarouselItem


class CarouselItemInline(admin.StackedInline):
    model = CarouselItem


class CarouselAdmin(admin.ModelAdmin):
    model = Carousel
    inlines = [CarouselItemInline]
    list_display = [
        'id',
        'name',
        'description',
    ]


admin.site.register(Carousel, CarouselAdmin)
