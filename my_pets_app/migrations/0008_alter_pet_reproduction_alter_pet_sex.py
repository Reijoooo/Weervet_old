# Generated by Django 5.0.4 on 2024-04-09 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_pets_app', '0007_alter_pet_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='reproduction',
            field=models.CharField(blank=True, choices=[('К', 'Кастрирован'), ('С', 'Стерилизована'), ('Н', 'Ничего')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='pet',
            name='sex',
            field=models.CharField(blank=True, choices=[('М', 'Мальчик'), ('Д', 'Девочка')], max_length=1, null=True),
        ),
    ]
