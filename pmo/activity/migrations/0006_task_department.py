# Generated by Django 5.1 on 2024-08-30 07:34

import django.db.models.deletion
from django.db import migrations, models

def get_default_department(apps, schema_editor):
    Department = apps.get_model('activity', 'Department')
    default_department = Department.objects.get(dept_name='se')  # Replace with your department name
    return default_department.id

class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0005_alter_profile_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='department',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='activity.department'),
        ),
    ]
