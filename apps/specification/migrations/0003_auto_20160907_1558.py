# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-07 15:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('specification', '0002_steering_wheel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brakes',
            options={'verbose_name': 'Brakes', 'verbose_name_plural': 'Brakes'},
        ),
    ]