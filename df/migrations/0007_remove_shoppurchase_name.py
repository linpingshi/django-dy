# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-09-06 06:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df', '0006_auto_20200906_1437'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppurchase',
            name='name',
        ),
    ]
