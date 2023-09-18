# Generated by Django 4.2.4 on 2023-09-16 02:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medicapp', '0024_doctor_user_alter_medical_doctor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='user',
        ),
        migrations.AlterField(
            model_name='medical',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='medical',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='medical',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medical', to='medicapp.medical'),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pat', to=settings.AUTH_USER_MODEL),
        ),
    ]