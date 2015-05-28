# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_agregador'),
    ]

    operations = [
        migrations.AddField(
            model_name='enlace',
            name='imagen',
            field=models.ImageField(default=1, upload_to=b'enlaces/'),
            preserve_default=False,
        ),
    ]
