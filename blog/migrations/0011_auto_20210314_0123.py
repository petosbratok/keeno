# Generated by Django 3.1 on 2021-03-13 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_post_content2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content2',
        ),
        migrations.AlterField(
            model_name='post',
            name='post_pic',
            field=models.ImageField(blank=True, upload_to='post_pics'),
        ),
    ]