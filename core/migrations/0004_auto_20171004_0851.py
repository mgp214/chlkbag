# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 15:51
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_area_area'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='region',
            name='contents',
        ),
        migrations.AddField(
            model_name='region',
            name='polygon',
            field=django.contrib.gis.db.models.fields.PolygonField(blank=True, default=None, geography=True, null=True, srid=4326, verbose_name='Polygon'),
        ),
    ]
