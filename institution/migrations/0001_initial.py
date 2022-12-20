# Generated by Django 4.0.6 on 2022-12-20 12:27

import core.helper.model_utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CofkUnionInstitution',
            fields=[
                ('institution_id', models.AutoField(primary_key=True, serialize=False)),
                ('institution_name', models.TextField()),
                ('institution_synonyms', models.TextField(blank=True, default='')),
                ('institution_city', models.TextField()),
                ('institution_city_synonyms', models.TextField(blank=True, default='')),
                ('institution_country', models.TextField()),
                ('institution_country_synonyms', models.TextField(blank=True, default='')),
                ('creation_timestamp', models.DateTimeField(blank=True, default=core.helper.model_utils.default_current_timestamp, null=True)),
                ('creation_user', models.CharField(max_length=50)),
                ('change_timestamp', models.DateTimeField(blank=True, default=core.helper.model_utils.default_current_timestamp, null=True)),
                ('change_user', models.CharField(max_length=50)),
                ('editors_notes', models.TextField(blank=True, null=True)),
                ('uuid', models.UUIDField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=1000, null=True)),
                ('latitude', models.CharField(blank=True, max_length=20, null=True)),
                ('longitude', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'cofk_union_institution',
            },
            bases=(models.Model, core.helper.model_utils.RecordTracker),
        ),
        migrations.CreateModel(
            name='CofkInstitutionResourceMap',
            fields=[
                ('recref_id', models.AutoField(primary_key=True, serialize=False)),
                ('from_date', models.DateField(null=True)),
                ('to_date', models.DateField(null=True)),
                ('relationship_type', models.CharField(max_length=100)),
                ('creation_timestamp', models.DateTimeField(blank=True, default=core.helper.model_utils.default_current_timestamp, null=True)),
                ('creation_user', models.CharField(max_length=50)),
                ('change_timestamp', models.DateTimeField(blank=True, default=core.helper.model_utils.default_current_timestamp, null=True)),
                ('change_user', models.CharField(max_length=50)),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institution.cofkunioninstitution')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cofkunionresource')),
            ],
            options={
                'db_table': 'cofk_institution_resource_map',
                'abstract': False,
            },
            bases=(models.Model, core.helper.model_utils.RecordTracker),
        ),
        migrations.CreateModel(
            name='CofkInstitutionImageMap',
            fields=[
                ('recref_id', models.AutoField(primary_key=True, serialize=False)),
                ('from_date', models.DateField(null=True)),
                ('to_date', models.DateField(null=True)),
                ('relationship_type', models.CharField(max_length=100)),
                ('creation_timestamp', models.DateTimeField(blank=True, default=core.helper.model_utils.default_current_timestamp, null=True)),
                ('creation_user', models.CharField(max_length=50)),
                ('change_timestamp', models.DateTimeField(blank=True, default=core.helper.model_utils.default_current_timestamp, null=True)),
                ('change_user', models.CharField(max_length=50)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cofkunionimage')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institution.cofkunioninstitution')),
            ],
            options={
                'db_table': 'cofk_institution_image_map',
                'abstract': False,
            },
            bases=(models.Model, core.helper.model_utils.RecordTracker),
        ),
    ]
