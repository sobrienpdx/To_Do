# Generated by Django 2.0 on 2018-08-24 18:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_app', '0002_auto_20180824_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 24, 11, 42, 51, 171833)),
        ),
    ]
