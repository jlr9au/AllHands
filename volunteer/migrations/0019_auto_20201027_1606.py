# Generated by Django 3.1.1 on 2020-10-27 20:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0018_auto_20201027_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteerevent',
            name='event_datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 27, 16, 6, 0, 641515)),
        ),
    ]
