# Generated by Django 3.1.3 on 2020-12-30 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KsiegarniaDB', '0007_auto_20201207_1400'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adres',
            options={'ordering': ('idAdresu',)},
        ),
        migrations.AlterModelOptions(
            name='kategoria',
            options={'ordering': ('idKategorii',)},
        ),
        migrations.AlterModelOptions(
            name='klient',
            options={'ordering': ('idKlienta',)},
        ),
        migrations.AlterModelOptions(
            name='ksiazka',
            options={'ordering': ('idKsiazki',)},
        ),
        migrations.AlterModelOptions(
            name='paragon',
            options={'ordering': ('idParagonu',)},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('idUsera',)},
        ),
    ]
