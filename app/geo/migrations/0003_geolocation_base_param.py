# Generated by Django 3.1.2 on 2022-02-12 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0002_auto_20220211_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='geolocation',
            name='base_param',
            field=models.CharField(default=None, max_length=500),
            preserve_default=False,
        ),
    ]