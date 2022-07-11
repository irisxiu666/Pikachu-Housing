# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('location', models.CharField(max_length=128, blank=True)),
                ('latitude', models.FloatField(default=0, null=True, blank=True, validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(-90)])),
                ('longitude', models.FloatField(default=0, null=True, blank=True, validators=[django.core.validators.MaxValueValidator(180), django.core.validators.MinValueValidator(-180)])),
            ],
        ),
    ]
