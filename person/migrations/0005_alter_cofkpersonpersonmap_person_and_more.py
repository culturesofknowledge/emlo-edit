# Generated by Django 4.0.6 on 2022-09-09 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0004_cofkpersonlocationmap_cofkunionperson_locations_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cofkpersonpersonmap',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='active_relationships', to='person.cofkunionperson', to_field='iperson_id'),
        ),
        migrations.AlterField(
            model_name='cofkpersonpersonmap',
            name='related',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passive_relationships', to='person.cofkunionperson', to_field='iperson_id'),
        ),
    ]