# Generated by Django 2.1.7 on 2019-03-05 01:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0002_auto_20190304_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateField(default=datetime.date(2019, 3, 4)),
        ),
    ]
