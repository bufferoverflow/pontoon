# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-18 12:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0057_stats_2_translated_resource'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resource',
            old_name='entity_count',
            new_name='total_strings',
        ),
        migrations.RenameField(
            model_name='translatedresource',
            old_name='approved_count',
            new_name='approved_strings',
        ),
        migrations.RenameField(
            model_name='translatedresource',
            old_name='fuzzy_count',
            new_name='fuzzy_strings',
        ),
        migrations.RenameField(
            model_name='translatedresource',
            old_name='translated_count',
            new_name='translated_strings',
        ),
        migrations.AlterField(
            model_name='translatedresource',
            name='locale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translatedresources', to='base.Locale'),
        ),
        migrations.AlterField(
            model_name='translatedresource',
            name='resource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translatedresources', to='base.Resource'),
        ),
    ]