# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-09-06 06:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('df', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='shoppurchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase', models.IntegerField(default=0, verbose_name='采购数量')),
                ('shop_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='df.shops', verbose_name='商品名称')),
            ],
            options={
                'verbose_name': '入库管理',
                'verbose_name_plural': '入库管理',
                'db_table': 'shops_purchase',
            },
        ),
    ]
