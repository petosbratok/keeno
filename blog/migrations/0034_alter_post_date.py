# Generated by Django 3.2.6 on 2022-07-20 12:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0033_alter_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 20, 15, 11, 55, 160236), null=True),
        ),
    ]
