# Generated by Django 5.0.4 on 2024-06-24 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acsess_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cse_staff',
            name='staff_email',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hdr_student',
            name='student_email',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
