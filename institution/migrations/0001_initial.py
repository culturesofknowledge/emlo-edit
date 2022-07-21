<<<<<<< HEAD
<<<<<<< HEAD
# Generated by Django 4.0.6 on 2022-08-02 15:11

import core.helper.model_utils
=======
# Generated by Django 4.0.6 on 2022-07-12 11:12
=======
# Generated by Django 4.0.6 on 2022-07-20 11:30
>>>>>>> a4a9ee0 (Error working)

>>>>>>> fb599c0 (Various)
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('uploader', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CofkUnionInstitution',
            fields=[
                ('institution_id', models.AutoField(primary_key=True, serialize=False)),
                ('institution_name', models.TextField()),
                ('institution_synonyms', models.TextField()),
                ('institution_city', models.TextField()),
                ('institution_city_synonyms', models.TextField()),
                ('institution_country', models.TextField()),
                ('institution_country_synonyms', models.TextField()),
                ('creation_timestamp', models.DateTimeField(blank=True, null=True)),
                ('creation_user', models.CharField(max_length=50)),
                ('change_timestamp', models.DateTimeField(blank=True, null=True)),
                ('change_user', models.CharField(max_length=50)),
                ('editors_notes', models.TextField(blank=True, null=True)),
                ('uuid', models.UUIDField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=1000, null=True)),
                ('latitude', models.CharField(blank=True, max_length=20, null=True)),
                ('longitude', models.CharField(blank=True, max_length=20, null=True)),
            ],
<<<<<<< HEAD
            options={
                'db_table': 'cofk_union_institution',
            },
            bases=(models.Model, core.helper.model_utils.RecordTracker),
=======
>>>>>>> fb599c0 (Various)
        ),
        migrations.CreateModel(
            name='CofkCollectInstitutionResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_id', models.IntegerField()),
                ('institution_id', models.IntegerField()),
                ('resource_name', models.TextField()),
                ('resource_details', models.TextField()),
                ('resource_url', models.TextField()),
                ('upload', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='uploader.cofkcollectupload')),
            ],
            options={
                'db_table': 'cofk_collect_institution_resource',
                'unique_together': {('upload', 'resource_id')},
            },
        ),
        migrations.CreateModel(
            name='CofkCollectInstitution',
            fields=[
                ('institution_id', models.AutoField(primary_key=True, serialize=False)),
                ('institution_name', models.TextField()),
                ('institution_city', models.TextField()),
                ('institution_country', models.TextField()),
                ('upload_name', models.CharField(blank=True, max_length=254, null=True)),
                ('_id', models.CharField(blank=True, max_length=32, null=True)),
                ('institution_synonyms', models.TextField(blank=True, null=True)),
                ('institution_city_synonyms', models.TextField(blank=True, null=True)),
                ('institution_country_synonyms', models.TextField(blank=True, null=True)),
                ('union_institution', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='institution.cofkunioninstitution')),
                ('upload', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploader.cofkcollectupload')),
            ],
            options={
                'db_table': 'cofk_collect_institution',
                'unique_together': {('upload', 'institution_id')},
            },
        ),
    ]
