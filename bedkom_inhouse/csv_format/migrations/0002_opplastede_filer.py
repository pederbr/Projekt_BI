# Generated by Django 5.0 on 2023-12-23 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csv_format', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='opplastede_filer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('navn', models.CharField(max_length=255)),
                ('fil', models.FileField(upload_to='static/CSV')),
            ],
        ),
    ]