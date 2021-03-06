# Generated by Django 3.1.1 on 2020-11-09 02:01

import datetime
from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('volunteer', '0025_merge_20201029_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteerevent',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='home repair, cooking, technology, yardwork, children', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='volunteerevent',
            name='event_datetime',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='volunteerevent',
            name='event_title',
            field=models.CharField(max_length=45),
        ),
    ]
