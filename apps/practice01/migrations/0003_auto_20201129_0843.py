# Generated by Django 3.1.3 on 2020-11-28 23:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('practice01', '0002_auto_20201128_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpractice',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 28, 23, 43, 6, 630038, tzinfo=utc)),
        ),
    ]
