# Generated by Django 3.0.2 on 2020-03-28 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity_periods',
            name='end_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='activity_periods',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]
