# Generated by Django 4.2.4 on 2023-08-17 00:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicapp', '0003_tbl_users'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_users',
        ),
    ]