# Generated by Django 5.0.4 on 2024-04-08 15:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('species', models.CharField(blank=True, max_length=50, null=True)),
                ('breed', models.CharField(blank=True, max_length=100, null=True)),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name=())),
                ('owner', models.CharField(blank=True, max_length=100, null=True)),
                ('color', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('microchip_number', models.CharField(blank=True, max_length=50, null=True)),
                ('date_microchip', models.DateField(blank=True, null=True, verbose_name=())),
                ('location_microchip', models.CharField(blank=True, max_length=50, null=True)),
                ('tattoo_number', models.CharField(blank=True, max_length=50, null=True)),
                ('date_tatoo', models.DateField(blank=True, null=True, verbose_name=())),
                ('special_marks', models.CharField(blank=True, max_length=150, null=True)),
                ('reproduction', models.CharField(blank=True, choices=[('C', 'Castration'), ('S', 'Sterilization'), ('N', 'Nothing')], max_length=1, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]