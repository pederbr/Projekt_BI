# Generated by Django 5.0 on 2024-01-03 21:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csv_format', '0013_bedrift_data_id_opplastede_filer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bedrift_data',
            name='id_opplastede_filer',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='opplastede_filer',
            name='dato_lagret',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 3, 22, 1, 20, 608039)),
        ),
    ]
