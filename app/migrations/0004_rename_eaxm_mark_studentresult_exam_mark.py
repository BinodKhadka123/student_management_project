# Generated by Django 5.0.1 on 2024-03-27 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_attendence_date_attendance_attendence_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentresult',
            old_name='eaxm_mark',
            new_name='exam_mark',
        ),
    ]
