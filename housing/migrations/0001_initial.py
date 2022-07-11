# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('location', models.CharField(max_length=128, blank=True)),
                ('price', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('cover_img', models.CharField(default=b'', max_length=512, blank=True)),
                ('types', models.CharField(max_length=64, blank=True)),
                ('description', models.CharField(max_length=1024, blank=True)),
                ('imgs_url', models.CharField(max_length=512, blank=True)),
                ('latitude', models.FloatField(default=0, null=True, blank=True, validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(-90)])),
                ('longitude', models.FloatField(default=0, null=True, blank=True, validators=[django.core.validators.MaxValueValidator(180), django.core.validators.MinValueValidator(-180)])),
                ('closest_department_float', models.FloatField(default=-1, null=True, blank=True)),
                ('provider', models.ForeignKey(blank=True, to='provider.Provider', null=True)),
            ],
        ),
    ]
