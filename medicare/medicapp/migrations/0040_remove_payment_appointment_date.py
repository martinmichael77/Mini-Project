# Generated by Django 4.2.4 on 2023-09-29 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicapp', '0039_payment_appointment_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='appointment_date',
        ),
    ]