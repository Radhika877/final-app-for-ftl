# Generated by Django 3.0.2 on 2020-03-29 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20200328_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]