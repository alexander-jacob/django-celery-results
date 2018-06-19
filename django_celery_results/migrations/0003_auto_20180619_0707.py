# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-19 07:07
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celery_results', '0002_add_task_name_args_kwargs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskresult',
            name='result',
            field=django.contrib.postgres.fields.jsonb.JSONField(editable=False, max_length=32768, null=True),
        ),
        migrations.AlterField(
            model_name='taskresult',
            name='task_kwargs',
            field=django.contrib.postgres.fields.jsonb.JSONField(max_length=32768, null=True, verbose_name='task kwargs'),
        ),
    ]