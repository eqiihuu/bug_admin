# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0014_auto_20151123_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stage',
            name='update_time',
            field=models.DateTimeField(verbose_name=b'Time updeted'),
        ),
    ]
