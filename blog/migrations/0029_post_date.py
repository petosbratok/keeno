# Generated by Django 3.2.6 on 2022-06-24 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_auto_20220622_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
