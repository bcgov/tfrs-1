# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-14 18:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_auto_20171214_1826'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='authorization_guid_new',
            new_name='authorization_guid',
        ),
        migrations.RemoveField(
            model_name='user',
            name='authorization_guid_old',
        ),
    ]