# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_create_history_tables'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalorder',
            name='payment_processor',
        ),
        migrations.RemoveField(
            model_name='order',
            name='payment_processor',
        ),
    ]
