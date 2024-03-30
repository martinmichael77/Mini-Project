# Generated by Django 4.2.4 on 2024-02-22 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicapp', '0050_appointmentcounselling_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('comments', models.TextField()),
                ('appointment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='medicapp.appointmentcounselling')),
            ],
        ),
    ]