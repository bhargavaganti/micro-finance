# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-08 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micro_admin', '0005_auto_20160708_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientbranchtransfer',
            name='changed_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]