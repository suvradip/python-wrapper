# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-03-22 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fusionCharts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('CountryCode', models.CharField(max_length=50)),
                ('District', models.CharField(max_length=50)),
                ('Population', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Code', models.CharField(max_length=50)),
                ('Population', models.CharField(max_length=50)),
            ],
        ),
    ]
