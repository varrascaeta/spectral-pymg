# Generated by Django 5.0.4 on 2024-05-05 20:13

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Raw Data', 'RAW'), ('Radiance', 'RAD'), ('Average Radiance', 'AVG_RAD'), ('Text Radiance', 'TXT_RAD'), ('Reflectance', 'REF'), ('Average Reflectance', 'AVG_REF'), ('Text Reflectance', 'TXT_REF')], max_length=128)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Coverage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('path', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('metadata', models.JSONField(null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MeasuringTool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('model_name', models.CharField(max_length=255, null=True)),
                ('fov', models.FloatField(null=True)),
                ('measure_height', models.FloatField(null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Spreadsheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('path', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('metadata', models.JSONField(null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sheet_type', models.CharField(choices=[('Office Sheet', 'OFC'), ('Field Sheet', 'FLD')], max_length=16)),
                ('delimiter', models.CharField(default=';', max_length=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('path', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('metadata', models.JSONField(null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateField(null=True)),
                ('external_id', models.CharField(max_length=255, null=True)),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='places.district')),
                ('coverage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coverage_campaigns', to='campaigns.coverage')),
                ('measuring_tool', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='campaigns', to='campaigns.measuringtool')),
                ('spreadsheets', models.ManyToManyField(blank=True, related_name='campaigns', to='campaigns.spreadsheet')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DataPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('path', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('metadata', models.JSONField(null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order', models.IntegerField()),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data_points', to='campaigns.campaign')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('path', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('metadata', models.JSONField(null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='campaigns.category')),
                ('data_points', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='campaigns.datapoint')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
