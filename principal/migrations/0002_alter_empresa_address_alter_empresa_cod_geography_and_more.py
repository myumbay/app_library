# Generated by Django 5.1 on 2023-11-09 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='cod_geography',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='logo',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]
