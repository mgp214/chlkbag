# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 22:01
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20170918_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='area',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(default=None, geography=True, null=True, srid=4326, verbose_name='Area'),
        ),
        migrations.AlterField(
            model_name='route',
            name='coordinates',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, default=None, geography=True, null=True, srid=4326, verbose_name='Coordinates'),
        ),
    ]
