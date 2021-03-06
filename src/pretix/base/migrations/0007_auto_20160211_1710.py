# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-11 17:10
from __future__ import unicode_literals

from decimal import Decimal

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0006_auto_20160211_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='tax_rate',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=7, verbose_name='Taxes included in percent'),
        ),
    ]
