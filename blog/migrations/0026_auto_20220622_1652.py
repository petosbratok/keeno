# Generated by Django 3.2.6 on 2022-06-22 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_auto_20220622_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='seats',
        ),
        migrations.RemoveField(
            model_name='post',
            name='theater_height',
        ),
        migrations.RemoveField(
            model_name='post',
            name='theater_width',
        ),
    ]