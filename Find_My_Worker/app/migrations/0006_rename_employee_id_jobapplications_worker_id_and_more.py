# Generated by Django 4.2.7 on 2023-12-12 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_customuser_job_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobapplications',
            old_name='employee_id',
            new_name='worker_id',
        ),
        migrations.RenameField(
            model_name='jobbooking',
            old_name='employee_id',
            new_name='worker_id',
        ),
        migrations.RenameField(
            model_name='reviews',
            old_name='employee_id',
            new_name='worker_id',
        ),
    ]
