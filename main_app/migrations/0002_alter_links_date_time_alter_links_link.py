# Generated by Django 5.0.7 on 2024-07-16 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='links',
            name='date_time',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='links',
            name='link',
            field=models.CharField(max_length=10000),
        ),
    ]
