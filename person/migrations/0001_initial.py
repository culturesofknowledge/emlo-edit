# Generated by Django 4.0.6 on 2022-12-19 13:44

import core.helper.model_utils
from django.db import migrations, models
import django.db.models.deletion
import functools


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('uploader', '0001_initial'),
        ('core', '0001_initial'),
        ('location', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CofkPersonLocationMap',
            fields=[
                ('recref_id', models.AutoField(primary_key=True, serialize=False)),
                ('from_date', models.DateField(null=True)),
                ('to_date', models.DateField(null=True)),
                ('relationship_type', models.CharField(max_length=100)),
                ('creation_timestamp', models.DateTimeField(blank=True, default=core.helper.model_utils.default_current_timestamp, null=True)),
                ('creation_user', models.CharField(max_length=50)),
                ('change_timestamp', models.DateTimeField(blank=True, default=core.helper.model_utils.default_current_timestamp, null=True)),
                ('change_user', models.CharField(max_length=50)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.cofkunionlocation')),
            ],
            options={
                'db_table': 'cofk_person_location_map',
                'abstract': False,
            },
            bases=(models.Model, core.helper.model_utils.RecordTracker),
        ),
        migrations.CreateModel(
            name='CofkUnionPerson',
            fields=[
                ('person_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('foaf_name', models.CharField(max_length=200)),
                ('skos_altlabel', models.TextField(blank=True, null=True)),
                ('skos_hiddenlabel', models.TextField(blank=True, null=True)),
                ('person_aliases', models.TextField(blank=True, null=True)),
                ('date_of_birth_year', models.IntegerField(blank=True, null=True)),
                ('date_of_birth_month', models.IntegerField(blank=True, null=True)),
                ('date_of_birth_day', models.IntegerField(blank=True, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_of_birth_inferred', models.SmallIntegerField(default=0)),
                ('date_of_birth_uncertain', models.SmallIntegerField(default=0)),
                ('date_of_birth_approx', models.SmallIntegerField(default=0)),
                ('date_of_death_year', models.IntegerField(blank=True, null=True)),
                ('date_of_death_month', models.IntegerField(blank=True, null=True)),
                ('date_of_death_day', models.IntegerField(blank=True, null=True)),
                ('date_of_death', models.DateField(blank=True, null=True)),
                ('date_of_death_inferred', models.SmallIntegerField(default=0)),
                ('date_of_death_uncertain', models.SmallIntegerField(default=0)),
                ('date_of_death_approx', models.SmallIntegerField(default=0)),
                ('gender', models.CharField(max_length=1)),
                ('is_organisation', models.CharField(max_length=1)),
                ('iperson_id', models.IntegerField(default=functools.partial(core.helper.model_utils.next_seq_safe, *('cofk_union_person_iperson_id_seq',), **{}), unique=True)),
                ('creation_timestamp', models.DateTimeField(blank=True, default=core.helper.model_utils.default_current_timestamp, null=True)),
                ('creation_user', models.CharField(max_length=50)),
                ('change_timestamp', models.DateTimeField(blank=True, default=core.helper.model_utils.default_current_timestamp, null=True)),
                ('change_user', models.CharField(max_length=50)),
                ('editors_notes', models.TextField(blank=True, null=True)),
                ('further_reading', models.TextField(blank=True, null=True)),
                ('date_of_birth_calendar', models.CharField(max_length=2)),
                ('date_of_birth_is_range', models.SmallIntegerField(default=0)),
                ('date_of_birth2_year', models.IntegerField(blank=True, null=True)),
                ('date_of_birth2_month', models.IntegerField(blank=True, null=True)),
                ('date_of_birth2_day', models.IntegerField(blank=True, null=True)),
                ('date_of_death_calendar', models.CharField(max_length=2)),
                ('date_of_death_is_range', models.SmallIntegerField(default=0)),
                ('date_of_death2_year', models.IntegerField(blank=True, null=True)),
                ('date_of_death2_month', models.IntegerField(blank=True, null=True)),
                ('date_of_death2_day', models.IntegerField(blank=True, null=True)),
                ('flourished', models.DateField(blank=True, null=True)),
                ('flourished_calendar', models.CharField(max_length=2)),
                ('flourished_is_range', models.SmallIntegerField(default=0)),
                ('flourished_year', models.IntegerField(blank=True, null=True)),
                ('flourished_month', models.IntegerField(blank=True, null=True)),
                ('flourished_day', models.IntegerField(blank=True, null=True)),
                ('flourished2_year', models.IntegerField(blank=True, null=True)),
                ('flourished2_month', models.IntegerField(blank=True, null=True)),
                ('flourished2_day', models.IntegerField(blank=True, null=True)),
                ('uuid', models.UUIDField(blank=True, null=True)),
                ('flourished_inferred', models.SmallIntegerField(default=0)),
                ('flourished_uncertain', models.SmallIntegerField(default=0)),
                ('flourished_approx', models.SmallIntegerField(default=0)),
                ('images', models.ManyToManyField(to='uploader.cofkunionimage')),
                ('locations', models.ManyToManyField(through='person.CofkPersonLocationMap', to='location.cofkunionlocation')),
                ('organisation_type', models.ForeignKey(blank=True, db_column='organisation_type', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='uploader.cofkunionorgtype')),
            ],
            options={
                'db_table': 'cofk_union_person',
            },
            bases=(models.Model, core.helper.model_utils.RecordTracker),
        ),
        migrations.CreateModel(
            name='CofkUnionPersonSummary',
            fields=[
                ('iperson', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='person.cofkunionperson')),
                ('other_details_summary', models.TextField(blank=True, null=True)),
                ('other_details_summary_searchable', models.TextField(blank=True, null=True)),
                ('sent', models.IntegerField()),
                ('recd', models.IntegerField()),
                ('all_works', models.IntegerField()),
                ('mentioned', models.IntegerField()),
                ('role_categories', models.TextField(blank=True, null=True)),
                ('images', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cofk_union_person_summary',
            },
        ),
        migrations.CreateModel(
            name='CofkPersonRoleMap',
            fields=[
                ('recref_id', models.AutoField(primary_key=True, serialize=False)),
                ('from_date', models.DateField(null=True)),
                ('to_date', models.DateField(null=True)),
                ('relationship_type', models.CharField(max_length=100)),
                ('creation_timestamp', models.DateTimeField(blank=True, default=core.helper.model_utils.default_current_timestamp, null=True)),
                ('creation_user', models.CharField(max_length=50)),
                ('change_timestamp', models.DateTimeField(blank=True, default=core.helper.model_utils.default_current_timestamp, null=True)),
                ('change_user', models.CharField(max_length=50)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.cofkunionperson')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploader.cofkunionrolecategory')),
            ],
            options={
                'db_table': 'cofk_person_role_map',
                'abstract': False,
            },
            bases=(models.Model, core.helper.model_utils.RecordTracker),
        ),
        migrations.CreateModel(
            name='CofkPersonResourceMap',
            fields=[
                ('recref_id', models.AutoField(primary_key=True, serialize=False)),
                ('from_date', models.DateField(null=True)),
                ('to_date', models.DateField(null=True)),
                ('relationship_type', models.CharField(max_length=100)),
                ('creation_timestamp', models.DateTimeField(blank=True, default=core.helper.model_utils.default_current_timestamp, null=True)),
                ('creation_user', models.CharField(max_length=50)),
                ('change_timestamp', models.DateTimeField(blank=True, default=core.helper.model_utils.default_current_timestamp, null=True)),
                ('change_user', models.CharField(max_length=50)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.cofkunionperson')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cofkunionresource')),
            ],
            options={
                'db_table': 'cofk_person_resource_map',
                'abstract': False,
            },
            bases=(models.Model, core.helper.model_utils.RecordTracker),
        ),
        migrations.CreateModel(
            name='CofkPersonPersonMap',
            fields=[
                ('recref_id', models.AutoField(primary_key=True, serialize=False)),
                ('from_date', models.DateField(null=True)),
                ('to_date', models.DateField(null=True)),
                ('relationship_type', models.CharField(max_length=100)),
                ('creation_timestamp', models.DateTimeField(blank=True, default=core.helper.model_utils.default_current_timestamp, null=True)),
                ('creation_user', models.CharField(max_length=50)),
                ('change_timestamp', models.DateTimeField(blank=True, default=core.helper.model_utils.default_current_timestamp, null=True)),
                ('change_user', models.CharField(max_length=50)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='active_relationships', to='person.cofkunionperson')),
                ('related', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passive_relationships', to='person.cofkunionperson')),
            ],
            options={
                'db_table': 'cofk_person_person_map',
                'abstract': False,
            },
            bases=(models.Model, core.helper.model_utils.RecordTracker),
        ),
        migrations.AddField(
            model_name='cofkpersonlocationmap',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.cofkunionperson'),
        ),
        migrations.CreateModel(
            name='CofkPersonImageMap',
            fields=[
                ('recref_id', models.AutoField(primary_key=True, serialize=False)),
                ('from_date', models.DateField(null=True)),
                ('to_date', models.DateField(null=True)),
                ('relationship_type', models.CharField(max_length=100)),
                ('creation_timestamp', models.DateTimeField(blank=True, default=core.helper.model_utils.default_current_timestamp, null=True)),
                ('creation_user', models.CharField(max_length=50)),
                ('change_timestamp', models.DateTimeField(blank=True, default=core.helper.model_utils.default_current_timestamp, null=True)),
                ('change_user', models.CharField(max_length=50)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploader.cofkunionimage')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.cofkunionperson')),
            ],
            options={
                'db_table': 'cofk_person_image_map',
                'abstract': False,
            },
            bases=(models.Model, core.helper.model_utils.RecordTracker),
        ),
        migrations.CreateModel(
            name='CofkPersonCommentMap',
            fields=[
                ('recref_id', models.AutoField(primary_key=True, serialize=False)),
                ('from_date', models.DateField(null=True)),
                ('to_date', models.DateField(null=True)),
                ('relationship_type', models.CharField(max_length=100)),
                ('creation_timestamp', models.DateTimeField(blank=True, default=core.helper.model_utils.default_current_timestamp, null=True)),
                ('creation_user', models.CharField(max_length=50)),
                ('change_timestamp', models.DateTimeField(blank=True, default=core.helper.model_utils.default_current_timestamp, null=True)),
                ('change_user', models.CharField(max_length=50)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cofkunioncomment')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.cofkunionperson')),
            ],
            options={
                'db_table': 'cofk_person_comment_map',
                'abstract': False,
            },
            bases=(models.Model, core.helper.model_utils.RecordTracker),
        ),
        migrations.CreateModel(
            name='CofkCollectPersonResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_id', models.IntegerField()),
                ('iperson_id', models.IntegerField()),
                ('resource_name', models.TextField()),
                ('resource_details', models.TextField()),
                ('resource_url', models.TextField()),
                ('upload', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='uploader.cofkcollectupload')),
            ],
            options={
                'db_table': 'cofk_collect_person_resource',
                'unique_together': {('upload', 'resource_id')},
            },
        ),
        migrations.CreateModel(
            name='CofkCollectPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iperson_id', models.IntegerField(blank=True, null=True)),
                ('primary_name', models.CharField(max_length=200)),
                ('alternative_names', models.TextField(blank=True, null=True)),
                ('roles_or_titles', models.TextField(blank=True, null=True)),
                ('gender', models.CharField(max_length=1)),
                ('is_organisation', models.CharField(max_length=1)),
                ('organisation_type', models.IntegerField(blank=True, null=True)),
                ('date_of_birth_year', models.IntegerField(blank=True, null=True)),
                ('date_of_birth_month', models.IntegerField(blank=True, null=True)),
                ('date_of_birth_day', models.IntegerField(blank=True, null=True)),
                ('date_of_birth_is_range', models.SmallIntegerField()),
                ('date_of_birth2_year', models.IntegerField(blank=True, null=True)),
                ('date_of_birth2_month', models.IntegerField(blank=True, null=True)),
                ('date_of_birth2_day', models.IntegerField(blank=True, null=True)),
                ('date_of_birth_inferred', models.SmallIntegerField()),
                ('date_of_birth_uncertain', models.SmallIntegerField()),
                ('date_of_birth_approx', models.SmallIntegerField()),
                ('date_of_death_year', models.IntegerField(blank=True, null=True)),
                ('date_of_death_month', models.IntegerField(blank=True, null=True)),
                ('date_of_death_day', models.IntegerField(blank=True, null=True)),
                ('date_of_death_is_range', models.SmallIntegerField()),
                ('date_of_death2_year', models.IntegerField(blank=True, null=True)),
                ('date_of_death2_month', models.IntegerField(blank=True, null=True)),
                ('date_of_death2_day', models.IntegerField(blank=True, null=True)),
                ('date_of_death_inferred', models.SmallIntegerField()),
                ('date_of_death_uncertain', models.SmallIntegerField()),
                ('date_of_death_approx', models.SmallIntegerField()),
                ('flourished_year', models.IntegerField(blank=True, null=True)),
                ('flourished_month', models.IntegerField(blank=True, null=True)),
                ('flourished_day', models.IntegerField(blank=True, null=True)),
                ('flourished_is_range', models.SmallIntegerField()),
                ('flourished2_year', models.IntegerField(blank=True, null=True)),
                ('flourished2_month', models.IntegerField(blank=True, null=True)),
                ('flourished2_day', models.IntegerField(blank=True, null=True)),
                ('notes_on_person', models.TextField(blank=True, null=True)),
                ('editors_notes', models.TextField(blank=True, null=True)),
                ('upload_name', models.CharField(blank=True, max_length=254, null=True)),
                ('_id', models.CharField(blank=True, max_length=32, null=True)),
                ('person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='collect_persons', to='person.cofkunionperson')),
                ('union_iperson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='union_collect_persons', to='person.cofkunionperson')),
                ('upload', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploader.cofkcollectupload')),
            ],
            options={
                'db_table': 'cofk_collect_person',
                'unique_together': {('upload', 'iperson_id')},
            },
        ),
        migrations.CreateModel(
            name='CofkCollectOccupationOfPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occupation_of_person_id', models.IntegerField()),
                ('iperson_id', models.IntegerField()),
                ('occupation', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='uploader.cofkunionrolecategory')),
                ('upload', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='uploader.cofkcollectupload')),
            ],
            options={
                'db_table': 'cofk_collect_occupation_of_person',
                'unique_together': {('upload', 'occupation_of_person_id')},
            },
        ),
    ]
