# Generated by Django 3.1.3 on 2020-12-06 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KsiegarniaDB', '0004_remove_user_email2'),
    ]

    operations = [
        migrations.AddField(
            model_name='paragon',
            name='dataWystawienia',
            field=models.DateTimeField(null=True),
        ),
    ]