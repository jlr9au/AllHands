# Generated by Django 3.1.1 on 2020-11-23 23:12

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('volunteer', '0029_auto_20201110_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteerevent',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='home repair, cooking, yardwork, children, school, technology, political, other', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]