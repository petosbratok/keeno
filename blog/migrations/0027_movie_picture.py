# Generated by Django 3.2.6 on 2022-06-22 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_auto_20220622_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='picture',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
