# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-01-19 23:06
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shuup_notify', '0005_shop_fill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shuup.Shop', verbose_name='shop'),
        ),
        migrations.AlterField(
            model_name='script',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shuup.Shop', verbose_name='shop'),
        ),
    ]
