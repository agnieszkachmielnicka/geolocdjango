# Generated by Django 3.1.2 on 2022-02-15 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0008_auto_20220215_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='geolocation',
            name='ip_url',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
    ]
