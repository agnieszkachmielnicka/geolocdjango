# Generated by Django 3.1.2 on 2022-02-15 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0007_delete_geolocation'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewLocation',
            new_name='GeoLocation',
        ),
    ]
