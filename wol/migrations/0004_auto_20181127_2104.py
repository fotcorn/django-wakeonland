# Generated by Django 2.1.3 on 2018-11-27 21:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wol', '0003_target_ip_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='target',
            name='ip_address',
            field=models.GenericIPAddressField(default='255.255.255.255', verbose_name='IP Address'),
        ),
        migrations.AlterField(
            model_name='target',
            name='mac_address',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(regex='^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$')], verbose_name='MAC Address'),
        ),
    ]
