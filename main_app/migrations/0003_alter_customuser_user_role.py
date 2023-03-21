# Generated by Django 4.1.7 on 2023-03-20 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_appointment_end_time_appointment_start_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_role',
            field=models.CharField(choices=[('admin', 'Admin'), ('doctor', 'Doctor'), ('patient', 'Patient')], default='patient', max_length=10),
        ),
    ]
