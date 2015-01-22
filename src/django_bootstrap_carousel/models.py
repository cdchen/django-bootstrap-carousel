# -*- coding: utf-8 -*-
from django.db import models


class Carousel(models.Model):
    name = models.CharField(
        max_length=64,
        db_index=True,
        unique=True,
    )

    interval = models.IntegerField(
        default=5000,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )


class CarouselItem(models.Model):
    class Meta:
        ordering = ['carousel', 'weight']

    carousel = models.ForeignKey(
        Carousel,
        related_name='items',
    )

    display_title = models.CharField(
        max_length=128,
    )

    display_content = models.TextField(
        null=True,
        blank=True,
    )

    url = models.URLField(
        null=True,
        blank=True,
    )

    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='carousel/',
    )

    weight = models.IntegerField(
        default=0,
        db_index=True,
    )

    activated = models.BooleanField(
        default=True,
        db_index=True,
    )
