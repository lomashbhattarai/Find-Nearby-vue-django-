# Generated by Django 2.1.5 on 2019-01-27 07:31

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0004_roadsegment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roadsegment',
            name='geom',
            field=django.contrib.gis.db.models.fields.MultiLineStringField(srid=4326),
        ),
    ]