# Generated by Django 3.1 on 2021-03-13 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
    ]