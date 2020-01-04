# Generated by Django 2.2 on 2020-01-04 18:24

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255, null=True), size=None),
        ),
        migrations.AlterField(
            model_name='movie',
            name='categories',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255, null=True), size=None),
        ),
    ]
