# Generated by Django 4.2.4 on 2024-03-17 01:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medicapp', '0060_counselingreport'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthMetric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metric_type', models.CharField(choices=[('weight', 'Weight'), ('blood_pressure', 'Blood Pressure'), ('blood_sugar', 'Blood Sugar')], max_length=100)),
                ('value', models.FloatField()),
                ('recorded_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='health_metrics', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='CounselingReport',
        ),
    ]