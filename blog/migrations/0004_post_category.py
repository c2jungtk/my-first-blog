# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-06 00:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(blank=True, choices=[('DJ', 'DJANGO'), ('PY', 'PYTHON'), ('GIT', 'GIT'), ('HTML', 'HTML'), ('PS', 'PHOTOSHOP')], max_length=20, null=True),
        ),
    ]