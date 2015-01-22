# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64, db_index=True)),
                ('interval', models.IntegerField(default=5000)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CarouselItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('display_title', models.CharField(max_length=128)),
                ('display_content', models.TextField(null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'carousel/', blank=True)),
                ('weight', models.IntegerField(default=0, db_index=True)),
                ('activated', models.BooleanField(default=True, db_index=True)),
                ('carousel', models.ForeignKey(related_name='items', to='django_bootstrap_carousel.Carousel')),
            ],
            options={
                'ordering': ['carousel', 'weight'],
            },
            bases=(models.Model,),
        ),
    ]
