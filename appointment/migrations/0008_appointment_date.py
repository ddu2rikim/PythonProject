# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-06 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0007_appointment_doctor_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='date',
            field=models.DateTimeField(auto_now_add=True, blank=True),
            preserve_default=False,
        ),
    ]