# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-11 19:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_auto_20180827_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificationmessage',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
    ]