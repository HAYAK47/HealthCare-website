# Generated by Django 4.1.7 on 2023-03-21 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_appointment_day_appointment_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='brief',
            field=models.TextField(max_length=5000),
        ),
    ]
