# Generated by Django 5.0.4 on 2024-07-16 10:12

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acsess_api', '0012_rename_room_booking_id_booking_booking_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotdesk',
            name='hotdesk_coordinates',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, null=True, size=None),
        ),
    ]
