# Generated by Django 4.2.4 on 2023-09-05 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicapp', '0010_rename_ment_day_treatment_treatment_day_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
