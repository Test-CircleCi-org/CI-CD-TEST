# Generated by Django 2.1.1 on 2018-10-04 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0005_auto_20181003_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campuspartner',
            name='weitz_cec_part',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default=False, max_length=6),
        ),
    ]
