# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='extra_field',
            field=models.BooleanField(default=False),
        ),
    ]
