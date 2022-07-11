# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0001_initial'),
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('distance', models.FloatField(default=0)),
                ('department_id', models.ForeignKey(related_name='distance', to='department.Department')),
                ('house_id', models.ForeignKey(related_name='distance', to='housing.House')),
            ],
        ),
    ]
