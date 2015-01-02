# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0003_photo_blocked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='owner',
            field=models.ForeignKey(related_name='galleries', to='instagram.Customer'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gallery',
            name='tag',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='gallery',
            field=models.ForeignKey(related_name='photos', to='instagram.Gallery'),
            preserve_default=True,
        ),
    ]
