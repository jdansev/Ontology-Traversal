# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-20 21:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GUI', '0005_auto_20170916_1425'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='defense_node',
            options={'ordering': ['-date_added']},
        ),
        migrations.AddField(
            model_name='attack_node',
            name='desc',
            field=models.CharField(default=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='defense_node',
            name='desc',
            field=models.CharField(max_length=500),
        ),
    ]
