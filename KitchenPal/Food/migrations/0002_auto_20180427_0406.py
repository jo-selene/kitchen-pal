# Generated by Django 2.0.3 on 2018-04-27 04:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='longevity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='longevityType',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='food',
            name='storageTips',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='food',
            name='storageType',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='food',
            name='type',
            field=models.CharField(default='Type', max_length=50),
            preserve_default=False,
        ),
    ]