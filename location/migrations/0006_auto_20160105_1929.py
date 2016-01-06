# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-05 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0005_auto_20160103_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicallocation',
            name='latitude',
            field=models.DecimalField(db_index=True, decimal_places=4, max_digits=7),
        ),
        migrations.AlterField(
            model_name='historicallocation',
            name='longitude',
            field=models.DecimalField(db_index=True, decimal_places=4, max_digits=8),
        ),
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.DecimalField(db_index=True, decimal_places=4, max_digits=7),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.DecimalField(db_index=True, decimal_places=4, max_digits=8),
        ),
    ]