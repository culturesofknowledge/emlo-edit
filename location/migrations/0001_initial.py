# Generated by Django 4.0.5 on 2022-06-17 08:42

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('uploader', '0002_remove_cofkcollectlocationresource_upload_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CofkUnionLocation',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('location_name', models.CharField(default='', max_length=500)),
                ('latitude', models.CharField(max_length=20)),
                ('longitude', models.CharField(max_length=20)),
                ('creation_timestamp', models.DateTimeField(auto_now=True)),
                ('change_timestamp', models.DateTimeField(auto_now=True)),
                ('location_synonyms', models.TextField()),
                ('editors_notes', models.TextField()),
                ('element_1_eg_room', models.CharField(default='', max_length=100)),
                ('element_2_eg_building', models.CharField(default='', max_length=100)),
                ('element_3_eg_parish', models.CharField(default='', max_length=100)),
                ('element_4_eg_city', models.CharField(default='', max_length=100)),
                ('element_5_eg_county', models.CharField(default='', max_length=100)),
                ('element_6_eg_country', models.CharField(default='', max_length=100)),
                ('element_7_eg_empire', models.CharField(default='', max_length=100)),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
            ],
            options={
                'db_table': 'cofk_union_location',
            },
        ),
        migrations.CreateModel(
            name='CofkCollectLocationResource',
            fields=[
                ('resource_id', models.AutoField(primary_key=True, serialize=False)),
                ('location_id', models.IntegerField()),
                ('resource_name', models.TextField(default='')),
                ('resource_details', models.TextField(default='')),
                ('resource_url', models.TextField(default='')),
                ('upload_id', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='uploader.cofkcollectupload')),
            ],
            options={
                'db_table': 'cofk_collect_location_resource',
            },
        ),
        migrations.CreateModel(
            name='CofkCollectLocation',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('location_name', models.CharField(default='', max_length=500)),
                ('element_1_eg_room', models.CharField(default='', max_length=100)),
                ('element_2_eg_building', models.CharField(default='', max_length=100)),
                ('element_3_eg_parish', models.CharField(default='', max_length=100)),
                ('element_4_eg_city', models.CharField(default='', max_length=100)),
                ('element_5_eg_county', models.CharField(default='', max_length=100)),
                ('element_6_eg_country', models.CharField(default='', max_length=100)),
                ('element_7_eg_empire', models.CharField(default='', max_length=100)),
                ('notes_on_place', models.TextField()),
                ('editors_notes', models.TextField()),
                ('upload_name', models.CharField(max_length=254)),
                ('_id', models.CharField(max_length=32)),
                ('location_synonyms', models.TextField()),
                ('latitude', models.CharField(max_length=20)),
                ('longitude', models.CharField(max_length=20)),
                ('union_location_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='location.cofkunionlocation')),
                ('upload_id', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='uploader.cofkcollectupload')),
            ],
            options={
                'db_table': 'cofk_collect_location',
            },
        ),
    ]
