# -*- coding: utf-8 -*-
from django.db import models


class Carousel(models.Model):
    pass


class CarouselElement(models.Model):

    carousel = models.ForeignKey(
        Carousel,
        related_name='elements',
    )

