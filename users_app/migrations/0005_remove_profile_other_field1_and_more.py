# Generated by Django 5.0.4 on 2024-04-08 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0004_profile_other_field1_profile_other_field2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='other_field1',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='other_field2',
        ),
    ]
