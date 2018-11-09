# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-23 20:43
from __future__ import unicode_literals

import db_comments.model_mixins
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0038_credittradehistory_user_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCreationRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_timestamp', models.DateTimeField(auto_now=True, null=True)),
                ('keycloak_email', models.EmailField(max_length=254, unique=True)),
                ('created', models.BooleanField(default=False)),
                ('create_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_usercreationrequest_CREATE_USER', to=settings.AUTH_USER_MODEL)),
                ('update_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_usercreationrequest_UPDATE_USER', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='creation_request', to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
                'db_table': 'user_creation_request',
            },
            bases=(models.Model, db_comments.model_mixins.DBComments),
        ),
    ]