# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0002_remove_photo_blocked'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='blocked',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
