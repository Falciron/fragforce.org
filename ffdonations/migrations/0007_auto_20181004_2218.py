# Generated by Django 2.1.2 on 2018-10-05 02:18

import datetime

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('ffdonations', '0006_auto_20181004_2159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donormodel',
            name='raw',
        ),
        migrations.AddField(
            model_name='donationmodel',
            name='amount',
            field=models.FloatField(default=0, null=True, verbose_name='Donation Amount'),
        ),
        migrations.AddField(
            model_name='donationmodel',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.utcnow, verbose_name='Created At'),
        ),
        migrations.AddField(
            model_name='donationmodel',
            name='donor',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING,
                                    to='ffdonations.DonorModel', verbose_name='Donor'),
        ),
        migrations.AddField(
            model_name='donationmodel',
            name='message',
            field=models.CharField(default='', max_length=1048576, verbose_name='Message'),
        ),
        migrations.AddField(
            model_name='donationmodel',
            name='participant',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING,
                                    to='ffdonations.ParticipantModel', verbose_name='Participant'),
        ),
        migrations.AddField(
            model_name='donationmodel',
            name='team',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING,
                                    to='ffdonations.TeamModel', verbose_name='Team'),
        ),
        migrations.AddField(
            model_name='donormodel',
            name='avatarImage',
            field=models.URLField(null=True, verbose_name='Avatar Image'),
        ),
        migrations.AddField(
            model_name='donormodel',
            name='displayName',
            field=models.CharField(max_length=8192, null=True, verbose_name='Donor Name'),
        ),
        migrations.AlterField(
            model_name='participantmodel',
            name='displayName',
            field=models.CharField(max_length=8192, null=True, verbose_name='Participant Name'),
        ),
    ]
