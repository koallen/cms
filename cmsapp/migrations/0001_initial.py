# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-19 07:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CallCenterReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mobile_number', models.CharField(max_length=8)),
                ('location', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('type_of_assistance', models.CharField(choices=[('EA', 'Emergency Ambulance'), ('RE', 'Rescue and Evacuation'), ('FF', 'Fire-fighting')], max_length=2)),
                ('status', models.NullBooleanField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Crisis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_crisis', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Decision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('type_of_crisis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmsapp.Crisis')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('decision', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmsapp.Decision')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('contact', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('place_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cmsapp.Place')),
            ],
            bases=('cmsapp.place',),
        ),
        migrations.CreateModel(
            name='UsefulPlace',
            fields=[
                ('place_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cmsapp.Place')),
                ('location', models.CharField(max_length=100)),
                ('type_of_place', models.CharField(choices=[('H', 'Hospital'), ('S', 'Shelter')], max_length=1)),
            ],
            bases=('cmsapp.place',),
        ),
        migrations.AddField(
            model_name='callcenterreport',
            name='type_of_crisis',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmsapp.Crisis'),
        ),
        migrations.AddField(
            model_name='notification',
            name='agency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmsapp.Agency'),
        ),
    ]