# Generated by Django 4.0.6 on 2024-10-22 11:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0008_alter_cofkunionlocation_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='cofkunionlocation',
            name='merged_master',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='merged_sources', to='location.cofkunionlocation'),
        ),
    ]
