# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-10 08:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190810_1652'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='modify_date',
            new_name='modify_datee',
        ),
    ]