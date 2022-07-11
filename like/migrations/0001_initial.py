# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('has_liked', models.BooleanField(default=True)),
                ('house_id', models.ForeignKey(related_name='liked_house', to='housing.House')),
                ('user_id', models.ForeignKey(related_name='liked_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
