# Generated by Django 2.1.2 on 2018-10-04 23:16

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
from django.contrib.postgres.operations import CreateExtension
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ('ffdonations', '0002_auto_20181004_1845'),
    ]

    operations = [
        CreateExtension('jsonb'),
        migrations.CreateModel(
            name='DonationModel',
            fields=[
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='GUID')),
                ('tracked', models.BooleanField(default=False, verbose_name='Is Tracked')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Date Record Last Fetched')),
                ('id',
                 models.BigIntegerField(editable=False, primary_key=True, serialize=False, verbose_name='Donation ID')),
                ('raw', django.contrib.postgres.fields.jsonb.JSONField(default={}, null=True, verbose_name='Raw Data')),
            ],
        ),
        migrations.CreateModel(
            name='DonorModel',
            fields=[
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='GUID')),
                ('tracked', models.BooleanField(default=False, verbose_name='Is Tracked')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Date Record Last Fetched')),
                ('id',
                 models.BigIntegerField(editable=False, primary_key=True, serialize=False, verbose_name='Donor ID')),
                ('raw', django.contrib.postgres.fields.jsonb.JSONField(default={}, null=True, verbose_name='Raw Data')),
            ],
        ),
        migrations.CreateModel(
            name='ParticipantModel',
            fields=[
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='GUID')),
                ('tracked', models.BooleanField(default=False, verbose_name='Is Tracked')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Date Record Last Fetched')),
                ('id', models.BigIntegerField(editable=False, primary_key=True, serialize=False,
                                              verbose_name='Participant ID')),
                ('raw', django.contrib.postgres.fields.jsonb.JSONField(default={}, null=True, verbose_name='Raw Data')),
            ],
        ),
        migrations.AddField(
            model_name='teammodel',
            name='raw',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}, null=True, verbose_name='Raw Data'),
        ),
    ]
