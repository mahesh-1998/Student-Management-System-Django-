# Generated by Django 2.2.5 on 2019-09-13 15:38

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_subject_prn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='subjects',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None),
        ),
    ]