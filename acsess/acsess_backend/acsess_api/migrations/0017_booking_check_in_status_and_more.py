# Generated by Django 5.0.4 on 2024-07-28 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acsess_api', '0016_cse_staff_otp_hdr_student_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='check_in_status',
            field=models.CharField(default='pending', max_length=20),
        ),
        migrations.AddField(
            model_name='booking_history',
            name='check_in_status',
            field=models.CharField(default='pending', max_length=20),
        ),
        migrations.AddField(
            model_name='booking_history',
            name='checked_in_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='booking_history',
            name='checked_out_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
