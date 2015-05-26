# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150524_1913'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agregador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=140)),
                ('enlaces', models.ManyToManyField(to='app.Enlace')),
            ],
        ),
    ]
