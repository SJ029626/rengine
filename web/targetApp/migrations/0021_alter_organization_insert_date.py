# Generated by Django 3.2.4 on 2021-07-09 01:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('targetApp', '0020_alter_organization_insert_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='insert_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 9, 1, 20, 20, 307493, tzinfo=utc)),
        ),
    ]
