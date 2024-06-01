# Generated by Django 5.0.4 on 2024-05-11 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0003_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Raw Data', 'Raw Data'), ('Radiance', 'Radiance'), ('Average Radiance', 'Average Radiance'), ('Text Radiance', 'Text Radiance'), ('Text Average Radiance', 'Text Average Radiance'), ('Reflectance', 'Reflectance'), ('Average Reflectance', 'Average Reflectance'), ('Text Reflectance', 'Text Reflectance'), ('Text Average Reflectance', 'Text Average Reflectance')], max_length=128),
        ),
    ]
