# Generated by Django 3.1.2 on 2022-02-15 14:33

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0003_geolocation_base_param'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_param', models.CharField(max_length=500)),
                ('geo_location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]