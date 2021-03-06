# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-09-05 10:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='shops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=20, unique=True, verbose_name='商品名称')),
                ('shop_number', models.IntegerField(verbose_name='商品数量')),
                ('shop_time', models.DateTimeField(verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '商品表',
                'verbose_name_plural': '商品表',
                'db_table': 'shops',
            },
        ),
    ]
