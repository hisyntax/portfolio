# Generated by Django 3.1b1 on 2020-11-24 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_backgroundimg_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='backgroundimg',
            name='title',
            field=models.CharField(default='hurrey', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logo',
            name='title',
            field=models.CharField(default='name', max_length=100),
            preserve_default=False,
        ),
    ]
