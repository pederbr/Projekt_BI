# Generated by Django 5.0 on 2023-12-25 12:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csv_format', '0005_alter_opplastede_filer_dato_lagret_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opplastede_filer',
            name='dato_lagret',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 25, 13, 4, 58, 779529)),
        ),
    ]
