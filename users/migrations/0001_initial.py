# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('department', models.ForeignKey(related_name='user', blank=True, to='department.Department', null=True)),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
                ('viewed_houses', models.ManyToManyField(related_name='viewed_user', to='housing.House', blank=True)),
            ],
        ),
    ]
