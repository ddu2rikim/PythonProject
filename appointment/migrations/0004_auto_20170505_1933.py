# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 23:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0003_auto_20170505_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='patient_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='patient.Patient'),
        ),
    ]