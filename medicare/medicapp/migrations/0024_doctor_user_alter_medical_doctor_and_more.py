# Generated by Django 4.2.4 on 2023-09-16 02:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medicapp', '0023_profile_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='doctor_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='medical',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='treated_patients', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='medical',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medical_records', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='treatments_approved', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='medical',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='treatments', to='medicapp.medical'),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='treatments', to=settings.AUTH_USER_MODEL),
        ),
    ]
