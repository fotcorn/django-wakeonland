# Generated by Django 2.1.3 on 2018-11-22 13:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wol', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='target',
            name='mac_address',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(regex='^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$')]),
        ),
    ]