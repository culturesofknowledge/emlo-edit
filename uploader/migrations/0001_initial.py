# Generated by Django 4.0.6 on 2022-07-08 12:23

from django.db import migrations, models
import django.db.models.deletion
import uploader.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CofkCollectStatus',
            fields=[
                ('status_id', models.AutoField(primary_key=True, serialize=False)),
                ('status_desc', models.CharField(max_length=100)),
                ('editable', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'cofk_collect_status',
            },
        ),
        migrations.CreateModel(
            name='CofkCollectToolUser',
            fields=[
                ('tool_user_id', models.AutoField(primary_key=True, serialize=False)),
                ('tool_user_email', models.CharField(max_length=100, unique=True)),
                ('tool_user_surname', models.CharField(max_length=100)),
                ('tool_user_forename', models.CharField(max_length=100)),
                ('tool_user_pw', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'cofk_collect_tool_user',
            },
        ),
        migrations.CreateModel(
            name='CofkLookupCatalogue',
            fields=[
                ('catalogue_id', models.AutoField(primary_key=True, serialize=False)),
                ('catalogue_code', models.CharField(default='', max_length=100, unique=True)),
                ('catalogue_name', models.CharField(default='', max_length=500, unique=True)),
                ('is_in_union', models.IntegerField(default=1)),
                ('publish_status', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'cofk_lookup_catalogue',
            },
        ),
        migrations.CreateModel(
            name='CofkReportGroup',
            fields=[
                ('report_group_id', models.AutoField(primary_key=True, serialize=False)),
                ('report_group_title', models.TextField()),
                ('report_group_order', models.IntegerField(default=1)),
                ('on_main_reports_menu', models.IntegerField(default=0)),
                ('report_group_code', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'cofk_report_groups',
            },
        ),
        migrations.CreateModel(
            name='CofkUnionAuditLiteral',
            fields=[
                ('audit_id', models.AutoField(primary_key=True, serialize=False)),
                ('change_timestamp', models.DateTimeField(auto_now=True)),
                ('change_type', models.CharField(max_length=3)),
                ('table_name', models.CharField(max_length=100)),
                ('key_value_text', models.CharField(max_length=100)),
                ('key_value_integer', models.IntegerField()),
                ('key_decode', models.TextField()),
                ('column_name', models.CharField(max_length=100)),
                ('new_column_value', models.TextField()),
                ('old_column_value', models.TextField()),
            ],
            options={
                'db_table': 'cofk_union_audit_literal',
            },
        ),
        migrations.CreateModel(
            name='CofkUnionAuditRelationship',
            fields=[
                ('audit_id', models.AutoField(primary_key=True, serialize=False)),
                ('change_timestamp', models.DateTimeField(auto_now=True)),
                ('change_type', models.CharField(max_length=3)),
                ('left_table_name', models.CharField(max_length=100)),
                ('left_id_value_new', models.CharField(default='', max_length=100)),
                ('left_id_decode_new', models.TextField(default='')),
                ('left_id_value_old', models.CharField(default='', max_length=100)),
                ('left_id_decode_old', models.TextField(default='')),
                ('relationship_type', models.CharField(max_length=100)),
                ('relationship_decode_left_to_right', models.CharField(default='', max_length=100)),
                ('relationship_decode_right_to_left', models.CharField(default='', max_length=100)),
                ('right_table_name', models.CharField(max_length=100)),
                ('right_id_value_new', models.CharField(default='', max_length=100)),
                ('right_id_decode_new', models.TextField(default='')),
                ('right_id_value_old', models.CharField(default='', max_length=100)),
                ('right_id_decode_old', models.TextField(default='')),
            ],
            options={
                'db_table': 'cofk_union_audit_relationship',
            },
        ),
        migrations.CreateModel(
            name='CofkUnionImage',
            fields=[
                ('image_id', models.AutoField(primary_key=True, serialize=False)),
                ('image_filename', models.TextField()),
                ('creation_timestamp', models.DateTimeField(auto_now=True)),
                ('change_timestamp', models.DateTimeField(auto_now=True)),
                ('thumbnail', models.TextField()),
                ('can_be_displayed', models.CharField(default='Y', max_length=1)),
                ('display_order', models.IntegerField(default=1)),
                ('licence_details', models.TextField(default='')),
                ('licence_url', models.CharField(default='', max_length=2000)),
                ('credits', models.CharField(default='', max_length=2000)),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
            ],
            options={
                'db_table': 'cofk_union_image',
            },
        ),
        migrations.CreateModel(
            name='CofkUnionOrgType',
            fields=[
                ('org_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('org_type_desc', models.CharField(default='', max_length=100)),
            ],
            options={
                'db_table': 'cofk_union_org_type',
            },
        ),
        migrations.CreateModel(
            name='CofkUnionPublication',
            fields=[
                ('publication_id', models.AutoField(primary_key=True, serialize=False)),
                ('publication_details', models.TextField(default='')),
                ('change_timestamp', models.DateTimeField(auto_now=True)),
                ('abbrev', models.CharField(default='', max_length=50)),
            ],
            options={
                'db_table': 'cofk_union_publication',
            },
        ),
        migrations.CreateModel(
            name='CofkUnionRoleCategory',
            fields=[
                ('role_category_id', models.AutoField(primary_key=True, serialize=False)),
                ('role_category_desc', models.CharField(default='', max_length=100)),
            ],
            options={
                'db_table': 'cofk_union_role_category',
            },
        ),
        migrations.CreateModel(
            name='CofkUnionSubject',
            fields=[
                ('subject_id', models.AutoField(primary_key=True, serialize=False)),
                ('subject_desc', models.CharField(default='', max_length=100)),
            ],
            options={
                'db_table': 'cofk_union_subject',
            },
        ),
        migrations.CreateModel(
            name='CofkUserSavedQuery',
            fields=[
                ('query_id', models.AutoField(primary_key=True, serialize=False)),
                ('query_class', models.CharField(max_length=100)),
                ('query_method', models.CharField(max_length=100)),
                ('query_title', models.TextField(default='')),
                ('query_order_by', models.CharField(default='', max_length=100)),
                ('query_sort_descending', models.SmallIntegerField(default=0)),
                ('query_entries_per_page', models.SmallIntegerField(default=20)),
                ('query_record_layout', models.CharField(default='across_page', max_length=12)),
                ('query_menu_item_name', models.TextField()),
                ('creation_timestamp', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'cofk_user_saved_queries',
            },
        ),
        migrations.CreateModel(
            name='Iso639LanguageCode',
            fields=[
                ('code_639_3', models.CharField(default='', max_length=3)),
                ('code_639_1', models.CharField(default='', max_length=2, null=True)),
                ('language_name', models.CharField(default='', max_length=100)),
                ('language_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'iso_639_language_codes',
            },
        ),
        migrations.CreateModel(
            name='CofkReport',
            fields=[
                ('report_id', models.AutoField(primary_key=True, serialize=False)),
                ('report_title', models.TextField()),
                ('class_name', models.CharField(max_length=40)),
                ('method_name', models.CharField(max_length=40)),
                ('has_csv_option', models.BooleanField(default=False)),
                ('is_dummy_option', models.BooleanField(default=False)),
                ('report_code', models.CharField(max_length=100)),
                ('parm_list', models.TextField()),
                ('parm_titles', models.TextField()),
                ('prompt_for_parms', models.SmallIntegerField(default=0)),
                ('default_parm_values', models.TextField()),
                ('parm_methods', models.TextField()),
                ('report_help', models.TextField()),
                ('report_group_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='uploader.cofkreportgroup')),
            ],
            options={
                'db_table': 'cofk_reports',
            },
        ),
        migrations.CreateModel(
            name='CofkCollectUpload',
            fields=[
                ('upload_id', models.AutoField(primary_key=True, serialize=False)),
                ('upload_username', models.CharField(max_length=100)),
                ('upload_description', models.TextField()),
                ('upload_timestamp', models.DateTimeField(auto_now=True)),
                ('total_works', models.IntegerField(default=0)),
                ('works_accepted', models.IntegerField(default=0)),
                ('works_rejected', models.IntegerField(default=0)),
                ('uploader_email', models.CharField(default='', max_length=250)),
                ('_id', models.CharField(max_length=32)),
                ('upload_name', models.CharField(max_length=254)),
                ('upload_file', models.FileField(upload_to=uploader.models.user_directory_path)),
                ('upload_status', models.ForeignKey(default='1', on_delete=django.db.models.deletion.DO_NOTHING, to='uploader.cofkcollectstatus')),
            ],
        ),
    ]
