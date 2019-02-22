# Generated by Django 2.1.5 on 2019-01-27 05:41

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0003_worldborder'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoadSegment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ntlclass', models.CharField(max_length=254)),
                ('srftpe', models.CharField(max_length=254)),
                ('segment', models.CharField(max_length=50)),
                ('geom', django.contrib.gis.db.models.fields.LineStringField(srid=4326)),
            ],
        ),
    ]
