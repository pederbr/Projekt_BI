# Generated by Django 5.0 on 2023-12-25 21:57

import datetime
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csv_format', '0006_alter_opplastede_filer_dato_lagret'),
    ]

    operations = [
        migrations.AddField(
            model_name='bedrift_data',
            name='dato_bedpres',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='opplastede_filer',
            name='dato_bedpres',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='opplastede_filer',
            name='dato_lagret',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 25, 22, 56, 44, 523116)),
        ),
    ]