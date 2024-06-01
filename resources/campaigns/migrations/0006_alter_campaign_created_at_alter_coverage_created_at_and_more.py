# Generated by Django 5.0.4 on 2024-05-20 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0005_campaign_ftp_created_at_coverage_ftp_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='coverage',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='datapoint',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='spreadsheet',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]