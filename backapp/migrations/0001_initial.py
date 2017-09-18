# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-18 15:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='table_manage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tablename', models.CharField(max_length=32)),
                ('ordertime', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='table_status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tablestatus', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='user_group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupname', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='user_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=32)),
                ('grouptype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backapp.user_group')),
            ],
        ),
        migrations.AddField(
            model_name='table_manage',
            name='ts',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backapp.table_status'),
        ),
    ]
