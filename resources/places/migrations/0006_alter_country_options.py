# Generated by Django 5.0.4 on 2024-06-11 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_alter_district_code_district_unique_district'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'Countries'},
        ),
    ]
