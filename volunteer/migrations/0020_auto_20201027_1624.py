# Generated by Django 3.1.1 on 2020-10-27 20:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0019_auto_20201027_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteerprofile',
            name='eventlist',
        ),
        migrations.AddField(
            model_name='volunteerprofile',
            name='events',
            field=models.ManyToManyField(to='volunteer.VolunteerEvent'),
        ),
        migrations.AlterField(
            model_name='volunteerevent',
            name='event_datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 27, 16, 24, 37, 288260)),
        ),
    ]
