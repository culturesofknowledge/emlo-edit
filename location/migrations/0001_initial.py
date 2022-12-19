# Generated by Django 4.0.6 on 2022-12-19 13:44

import core.helper.model_utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CofkCollectLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_id', models.IntegerField()),
                ('location_name', models.CharField(max_length=500)),
                ('element_1_eg_room', models.CharField(max_length=100)),
                ('element_2_eg_building', models.CharField(max_length=100)),
                ('element_3_eg_parish', models.CharField(max_length=100)),
                ('element_4_eg_city', models.CharField(max_length=100)),
                ('element_5_eg_county', models.CharField(max_length=100)),
                ('element_6_eg_country', models.CharField(max_length=100)),
                ('element_7_eg_empire', models.CharField(max_length=100)),
                ('notes_on_place', models.TextField(blank=True, null=True)),
                ('editors_notes', models.TextField(blank=True, null=True)),
                ('upload_name', models.CharField(blank=True, max_length=254, null=True)),
                ('_id', models.CharField(blank=True, max_length=32, null=True)),
                ('location_synonyms', models.TextField(blank=True, null=True)),
                ('latitude', models.CharField(blank=True, max_length=20, null=True)),
                ('longitude', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'cofk_collect_location',
            },
        ),
        migrations.CreateModel(
            name='CofkCollectLocationResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_id', models.IntegerField()),
                ('location_id', models.IntegerField()),
                ('resource_name', models.TextField()),
                ('resource_details', models.TextField()),
                ('resource_url', models.TextField()),
            ],
            options={
                'db_table': 'cofk_collect_location_resource',
            },
        ),
        migrations.CreateModel(
            name='CofkLocationCommentMap',
            fields=[
                ('recref_id', models.AutoField(primary_key=True, serialize=False)),
                ('from_date', models.DateField(null=True)),
                ('to_date', models.DateField(null=True)),
                ('relationship_type', models.CharField(max_length=100)),
                ('creation_timestamp', models.DateTimeField(blank=True, default=core.helper.model_utils.default_current_timestamp, null=True)),
                ('creation_user', models.CharField(max_length=50)),
                ('change_timestamp', models.DateTimeField(blank=True, default=core.helper.model_utils.default_current_timestamp, null=True)),
                ('change_user', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'cofk_location_comment_map',
                'abstract': False,
            },
            bases=(models.Model, core.helper.model_utils.RecordTracker),
        ),
        migrations.CreateModel(
            name='CofkLocationImageMap',
            fields=[
                ('recref_id', models.AutoField(primary_key=True, serialize=False)),
                ('from_date', models.DateField(null=True)),
                ('to_date', models.DateField(null=True)),
                ('relationship_type', models.CharField(max_length=100)),
                ('creation_timestamp', models.DateTimeField(blank=True, default=core.helper.model_utils.default_current_timestamp, null=True)),
                ('creation_user', models.CharField(max_length=50)),
                ('change_timestamp', models.DateTimeField(blank=True, default=core.helper.model_utils.default_current_timestamp, null=True)),
                ('change_user', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'cofk_location_image_map',
                'abstract': False,
            },
            bases=(models.Model, core.helper.model_utils.RecordTracker),
        ),
        migrations.CreateModel(
            name='CofkLocationResourceMap',
            fields=[
                ('recref_id', models.AutoField(primary_key=True, serialize=False)),
                ('from_date', models.DateField(null=True)),
                ('to_date', models.DateField(null=True)),
                ('relationship_type', models.CharField(max_length=100)),
                ('creation_timestamp', models.DateTimeField(blank=True, default=core.helper.model_utils.default_current_timestamp, null=True)),
                ('creation_user', models.CharField(max_length=50)),
                ('change_timestamp', models.DateTimeField(blank=True, default=core.helper.model_utils.default_current_timestamp, null=True)),
                ('change_user', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'cofk_location_resource_map',
                'abstract': False,
            },
            bases=(models.Model, core.helper.model_utils.RecordTracker),
        ),
        migrations.CreateModel(
            name='CofkUnionLocation',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('location_name', models.CharField(max_length=500)),
                ('latitude', models.CharField(blank=True, max_length=20, null=True)),
                ('longitude', models.CharField(blank=True, max_length=20, null=True)),
                ('creation_timestamp', models.DateTimeField(blank=True, default=core.helper.model_utils.default_current_timestamp, null=True)),
                ('creation_user', models.CharField(max_length=50)),
                ('change_timestamp', models.DateTimeField(blank=True, default=core.helper.model_utils.default_current_timestamp, null=True)),
                ('change_user', models.CharField(max_length=50)),
                ('location_synonyms', models.TextField(blank=True, null=True)),
                ('editors_notes', models.TextField(blank=True, null=True)),
                ('element_1_eg_room', models.CharField(max_length=100)),
                ('element_2_eg_building', models.CharField(max_length=100)),
                ('element_3_eg_parish', models.CharField(max_length=100)),
                ('element_4_eg_city', models.CharField(max_length=100)),
                ('element_5_eg_county', models.CharField(max_length=100)),
                ('element_6_eg_country', models.CharField(max_length=100)),
                ('element_7_eg_empire', models.CharField(max_length=100)),
                ('uuid', models.UUIDField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cofk_union_location',
            },
            bases=(models.Model, core.helper.model_utils.RecordTracker),
        ),
    ]
