# Generated by Django 4.0.6 on 2024-09-23 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tombstone', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tombstonerequest',
            name='sql_params',
            field=models.BinaryField(blank=True, null=True),
        ),
    ]