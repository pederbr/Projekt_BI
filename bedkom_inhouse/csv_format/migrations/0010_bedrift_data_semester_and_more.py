# Generated by Django 5.0 on 2023-12-26 21:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csv_format', '0009_alter_bedrift_data_dato_bedpres_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bedrift_data',
            name='semester',
            field=models.CharField(default='h23', max_length=255),
        ),
        migrations.AlterField(
            model_name='opplastede_filer',
            name='dato_lagret',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 26, 22, 31, 37, 992699)),
        ),
    ]
