# Generated by Django 5.0.4 on 2024-04-09 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0009_myevent_creator_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myevent',
            old_name='creator_id',
            new_name='user',
        ),
    ]
