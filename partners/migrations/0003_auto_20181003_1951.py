# Generated by Django 2.1.1 on 2018-10-04 00:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0002_auto_20181002_1916'),
    ]

    operations = [
        migrations.RenameField(
            model_name='communitypartner',
            old_name='country',
            new_name='county',
        ),
        migrations.RenameField(
            model_name='communitypartner',
            old_name='Zip',
            new_name='zip',
        ),
    ]
