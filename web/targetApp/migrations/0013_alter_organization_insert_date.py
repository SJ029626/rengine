# Generated by Django 3.2.4 on 2021-07-08 05:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('targetApp', '0012_auto_20210708_0453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='insert_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 8, 5, 13, 16, 420536, tzinfo=utc)),
        ),
    ]
