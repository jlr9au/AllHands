# Generated by Django 3.1.1 on 2020-10-21 19:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0009_auto_20201021_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteerevent',
            name='event_datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 21, 15, 53, 38, 622904)),
        ),
    ]
