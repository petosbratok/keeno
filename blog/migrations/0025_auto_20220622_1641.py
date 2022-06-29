# Generated by Django 3.2.6 on 2022-06-22 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_auto_20220622_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('theater_height', models.IntegerField(blank=True)),
                ('theater_width', models.IntegerField(blank=True)),
                ('seats', models.TextField(blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='description',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.RemoveField(
            model_name='post',
            name='trailer_link',
        ),
        migrations.AlterField(
            model_name='movie',
            name='author',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='movie',
            name='trailer_link',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='theater',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.theater'),
        ),
    ]