# Generated by Django 3.1.3 on 2021-01-12 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KsiegarniaDB', '0003_auto_20210112_1613'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.RemoveField(
            model_name='user',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
