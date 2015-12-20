# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-19 04:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('continent', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Population',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveIntegerField()),
                ('population', models.PositiveIntegerField()),
                ('continent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Continent')),
            ],
        ),
    ]