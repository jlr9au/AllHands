# Generated by Django 3.1.1 on 2020-10-17 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VolunteerEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(max_length=25)),
                ('event_datetime', models.DateTimeField()),
            ],
        ),
    ]