# Generated by Django 4.2.4 on 2023-09-15 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicapp', '0022_doctor_email_doctor_first_name_doctor_last_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]