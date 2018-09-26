# Generated by Django 2.1.1 on 2018-09-26 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0001_initial'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='campuspartnercontact',
            name='partner_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='partners.CampusPartner'),
        ),
        migrations.AddField(
            model_name='contact',
            name='CommunityPartnerName',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='partners.CommunityPartner'),
        ),
    ]
