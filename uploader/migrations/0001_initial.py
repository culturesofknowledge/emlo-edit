# Generated by Django 4.0.6 on 2022-12-20 12:27

from django.db import migrations, models
import django.db.models.deletion
import uploader.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        ('location', '0001_initial'),
        ('work', '0001_initial'),
        ('person', '0001_initial'),
        ('manifestation', '0001_initial'),
        ('institution', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CofkCollectDestinationOfWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination_id', models.IntegerField()),
                ('notes_on_destination', models.TextField(blank=True, null=True)),
                ('_id', models.CharField(blank=True, max_length=32, null=True)),
            ],
            options={
                'db_table': 'cofk_collect_destination_of_work',
            },
        ),
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
                ('union_location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='location.cofkunionlocation')),
            ],
            options={
                'db_table': 'cofk_collect_location',
            },
        ),
        migrations.CreateModel(
            name='CofkCollectOriginOfWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin_id', models.IntegerField()),
                ('notes_on_origin', models.TextField(blank=True, null=True)),
                ('_id', models.CharField(blank=True, max_length=32, null=True)),
            ],
            options={
                'db_table': 'cofk_collect_origin_of_work',
            },
        ),
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
            name='CofkCollectUpload',
            fields=[
                ('upload_id', models.AutoField(primary_key=True, serialize=False)),
                ('upload_username', models.CharField(max_length=100)),
                ('upload_description', models.TextField(blank=True, null=True)),
                ('upload_timestamp', models.DateTimeField()),
                ('total_works', models.IntegerField()),
                ('works_accepted', models.IntegerField()),
                ('works_rejected', models.IntegerField()),
                ('uploader_email', models.CharField(max_length=250)),
                ('_id', models.CharField(blank=True, max_length=32, null=True)),
                ('upload_name', models.CharField(blank=True, max_length=254, null=True)),
                ('upload_file', models.FileField(upload_to=uploader.models.user_directory_path)),
                ('upload_status', models.ForeignKey(db_column='upload_status', on_delete=django.db.models.deletion.DO_NOTHING, to='uploader.cofkcollectstatus')),
            ],
            options={
                'db_table': 'cofk_collect_upload',
            },
        ),
        migrations.CreateModel(
            name='CofkCollectWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iwork_id', models.IntegerField()),
                ('date_of_work_as_marked', models.CharField(blank=True, max_length=250, null=True)),
                ('original_calendar', models.CharField(blank=True, max_length=2)),
                ('date_of_work_std_year', models.IntegerField(blank=True, null=True)),
                ('date_of_work_std_month', models.IntegerField(blank=True, null=True)),
                ('date_of_work_std_day', models.IntegerField(blank=True, null=True)),
                ('date_of_work2_std_year', models.IntegerField(blank=True, null=True)),
                ('date_of_work2_std_month', models.IntegerField(blank=True, null=True)),
                ('date_of_work2_std_day', models.IntegerField(blank=True, null=True)),
                ('date_of_work_std_is_range', models.SmallIntegerField()),
                ('date_of_work_inferred', models.SmallIntegerField()),
                ('date_of_work_uncertain', models.SmallIntegerField()),
                ('date_of_work_approx', models.SmallIntegerField()),
                ('notes_on_date_of_work', models.TextField(blank=True, null=True)),
                ('authors_as_marked', models.TextField(blank=True, null=True)),
                ('authors_inferred', models.SmallIntegerField()),
                ('authors_uncertain', models.SmallIntegerField()),
                ('notes_on_authors', models.TextField(blank=True, null=True)),
                ('addressees_as_marked', models.TextField(blank=True, null=True)),
                ('addressees_inferred', models.SmallIntegerField()),
                ('addressees_uncertain', models.SmallIntegerField()),
                ('notes_on_addressees', models.TextField(blank=True, null=True)),
                ('destination_as_marked', models.TextField(blank=True, null=True)),
                ('destination_inferred', models.SmallIntegerField()),
                ('destination_uncertain', models.SmallIntegerField()),
                ('origin_as_marked', models.TextField(blank=True, null=True)),
                ('origin_inferred', models.SmallIntegerField()),
                ('origin_uncertain', models.SmallIntegerField()),
                ('abstract', models.TextField(blank=True, null=True)),
                ('keywords', models.TextField(blank=True, null=True)),
                ('language_of_work', models.CharField(blank=True, max_length=255, null=True)),
                ('incipit', models.TextField(blank=True, null=True)),
                ('excipit', models.TextField(blank=True, null=True)),
                ('accession_code', models.CharField(blank=True, max_length=250, null=True)),
                ('notes_on_letter', models.TextField(blank=True, null=True)),
                ('notes_on_people_mentioned', models.TextField(blank=True, null=True)),
                ('editors_notes', models.TextField(blank=True, null=True)),
                ('_id', models.CharField(blank=True, db_column='_id', max_length=32, null=True)),
                ('date_of_work2_approx', models.SmallIntegerField()),
                ('date_of_work2_inferred', models.SmallIntegerField()),
                ('date_of_work2_uncertain', models.SmallIntegerField()),
                ('mentioned_as_marked', models.TextField(blank=True, null=True)),
                ('mentioned_inferred', models.SmallIntegerField()),
                ('mentioned_uncertain', models.SmallIntegerField()),
                ('notes_on_destination', models.TextField(blank=True, null=True)),
                ('notes_on_origin', models.TextField(blank=True, null=True)),
                ('notes_on_place_mentioned', models.TextField(blank=True, null=True)),
                ('place_mentioned_as_marked', models.TextField(blank=True, null=True)),
                ('place_mentioned_inferred', models.SmallIntegerField()),
                ('place_mentioned_uncertain', models.SmallIntegerField()),
                ('upload_name', models.CharField(blank=True, max_length=254, null=True)),
                ('explicit', models.TextField(blank=True, null=True)),
                ('destination', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='uploader.cofkcollectdestinationofwork')),
                ('origin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='uploader.cofkcollectoriginofwork')),
                ('union_iwork', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='union_collect_works', to='work.cofkunionwork')),
                ('upload', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploader.cofkcollectupload')),
                ('upload_status', models.ForeignKey(db_column='upload_status', on_delete=django.db.models.deletion.DO_NOTHING, to='uploader.cofkcollectstatus')),
                ('work', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='collect_works', to='work.cofkunionwork')),
            ],
            options={
                'db_table': 'cofk_collect_work',
                'unique_together': {('upload', 'iwork_id')},
            },
        ),
        migrations.CreateModel(
            name='CofkCollectToolSession',
            fields=[
                ('session_id', models.AutoField(primary_key=True, serialize=False)),
                ('session_timestamp', models.DateTimeField()),
                ('session_code', models.TextField(blank=True, null=True, unique=True)),
                ('username', models.ForeignKey(blank=True, db_column='username', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='uploader.cofkcollecttooluser')),
            ],
            options={
                'db_table': 'cofk_collect_tool_session',
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
        migrations.AddField(
            model_name='cofkcollectoriginofwork',
            name='iwork',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploader.cofkcollectwork'),
        ),
        migrations.AddField(
            model_name='cofkcollectoriginofwork',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploader.cofkcollectlocation'),
        ),
        migrations.AddField(
            model_name='cofkcollectoriginofwork',
            name='upload',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploader.cofkcollectupload'),
        ),
        migrations.AddField(
            model_name='cofkcollectlocation',
            name='upload',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='uploader.cofkcollectupload'),
        ),
        migrations.CreateModel(
            name='CofkCollectInstitution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_id', models.IntegerField()),
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
        migrations.CreateModel(
            name='CofkCollectImageOfManif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manifestation_id', models.IntegerField()),
                ('image_filename', models.CharField(max_length=2000)),
                ('_id', models.CharField(blank=True, max_length=32, null=True)),
                ('iwork_id', models.IntegerField(blank=True, null=True)),
                ('upload', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='uploader.cofkcollectupload')),
            ],
            options={
                'db_table': 'cofk_collect_image_of_manif',
            },
        ),
        migrations.AddField(
            model_name='cofkcollectdestinationofwork',
            name='iwork',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploader.cofkcollectwork'),
        ),
        migrations.AddField(
            model_name='cofkcollectdestinationofwork',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploader.cofkcollectlocation'),
        ),
        migrations.AddField(
            model_name='cofkcollectdestinationofwork',
            name='upload',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploader.cofkcollectupload'),
        ),
        migrations.CreateModel(
            name='CofkCollectWorkSummary',
            fields=[
                ('upload', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='uploader.cofkcollectwork')),
                ('work_id_in_tool', models.IntegerField()),
                ('source_of_data', models.CharField(blank=True, max_length=250, null=True)),
                ('notes_on_letter', models.TextField(blank=True, null=True)),
                ('date_of_work', models.CharField(blank=True, max_length=32, null=True)),
                ('date_of_work_as_marked', models.CharField(blank=True, max_length=250, null=True)),
                ('original_calendar', models.CharField(blank=True, max_length=30, null=True)),
                ('date_of_work_is_range', models.CharField(blank=True, max_length=30, null=True)),
                ('date_of_work_inferred', models.CharField(blank=True, max_length=30, null=True)),
                ('date_of_work_uncertain', models.CharField(blank=True, max_length=30, null=True)),
                ('date_of_work_approx', models.CharField(blank=True, max_length=30, null=True)),
                ('notes_on_date_of_work', models.TextField(blank=True, null=True)),
                ('authors', models.TextField(blank=True, null=True)),
                ('authors_as_marked', models.TextField(blank=True, null=True)),
                ('authors_inferred', models.CharField(blank=True, max_length=30, null=True)),
                ('authors_uncertain', models.CharField(blank=True, max_length=30, null=True)),
                ('notes_on_authors', models.TextField(blank=True, null=True)),
                ('addressees', models.TextField(blank=True, null=True)),
                ('addressees_as_marked', models.TextField(blank=True, null=True)),
                ('addressees_inferred', models.CharField(blank=True, max_length=30, null=True)),
                ('addressees_uncertain', models.CharField(blank=True, max_length=30, null=True)),
                ('notes_on_addressees', models.TextField(blank=True, null=True)),
                ('destination', models.TextField(blank=True, null=True)),
                ('destination_as_marked', models.TextField(blank=True, null=True)),
                ('destination_inferred', models.CharField(blank=True, max_length=30, null=True)),
                ('destination_uncertain', models.CharField(blank=True, max_length=30, null=True)),
                ('origin', models.TextField(blank=True, null=True)),
                ('origin_as_marked', models.TextField(blank=True, null=True)),
                ('origin_inferred', models.CharField(blank=True, max_length=30, null=True)),
                ('origin_uncertain', models.CharField(blank=True, max_length=30, null=True)),
                ('abstract', models.TextField(blank=True, null=True)),
                ('keywords', models.TextField(blank=True, null=True)),
                ('languages_of_work', models.TextField(blank=True, null=True)),
                ('subjects_of_work', models.TextField(blank=True, null=True)),
                ('incipit', models.TextField(blank=True, null=True)),
                ('excipit', models.TextField(blank=True, null=True)),
                ('people_mentioned', models.TextField(blank=True, null=True)),
                ('notes_on_people_mentioned', models.TextField(blank=True, null=True)),
                ('places_mentioned', models.TextField(blank=True, null=True)),
                ('manifestations', models.TextField(blank=True, null=True)),
                ('related_resources', models.TextField(blank=True, null=True)),
                ('editors_notes', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cofk_collect_work_summary',
                'unique_together': {('upload', 'work_id_in_tool')},
            },
        ),
        migrations.CreateModel(
            name='CofkCollectWorkResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_id', models.IntegerField()),
                ('resource_name', models.TextField()),
                ('resource_details', models.TextField()),
                ('resource_url', models.TextField()),
                ('_id', models.CharField(blank=True, max_length=32, null=True)),
                ('iwork', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploader.cofkcollectwork')),
                ('upload', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploader.cofkcollectupload')),
            ],
            options={
                'db_table': 'cofk_collect_work_resource',
                'unique_together': {('upload', 'iwork_id', 'resource_id')},
            },
        ),
        migrations.CreateModel(
            name='CofkCollectSubjectOfWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_of_work_id', models.IntegerField()),
                ('iwork_id', models.IntegerField()),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.cofkunionsubject')),
                ('upload', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploader.cofkcollectupload')),
            ],
            options={
                'db_table': 'cofk_collect_subject_of_work',
                'unique_together': {('upload', 'iwork_id', 'subject_of_work_id')},
            },
        ),
        migrations.CreateModel(
            name='CofkCollectPlaceMentionedInWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mention_id', models.IntegerField()),
                ('location_id', models.IntegerField()),
                ('iwork_id', models.IntegerField()),
                ('notes_on_place_mentioned', models.TextField(blank=True, null=True)),
                ('_id', models.CharField(blank=True, max_length=32, null=True)),
                ('upload', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploader.cofkcollectupload')),
            ],
            options={
                'db_table': 'cofk_collect_place_mentioned_in_work',
                'unique_together': {('upload', 'iwork_id', 'mention_id')},
            },
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
            name='CofkCollectPersonMentionedInWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mention_id', models.IntegerField()),
                ('notes_on_person_mentioned', models.TextField(blank=True, null=True)),
                ('_id', models.CharField(max_length=32, null=True)),
                ('iperson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploader.cofkcollectperson')),
                ('iwork', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploader.cofkcollectwork')),
                ('upload', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploader.cofkcollectupload')),
            ],
            options={
                'db_table': 'cofk_collect_person_mentioned_in_work',
                'unique_together': {('upload', 'iwork_id', 'mention_id')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='cofkcollectoriginofwork',
            unique_together={('upload', 'iwork', 'origin_id')},
        ),
        migrations.CreateModel(
            name='CofkCollectOccupationOfPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occupation_of_person_id', models.IntegerField()),
                ('iperson_id', models.IntegerField()),
                ('occupation', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.cofkunionrolecategory')),
                ('upload', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='uploader.cofkcollectupload')),
            ],
            options={
                'db_table': 'cofk_collect_occupation_of_person',
                'unique_together': {('upload', 'occupation_of_person_id')},
            },
        ),
        migrations.CreateModel(
            name='CofkCollectManifestation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manifestation_id', models.IntegerField()),
                ('manifestation_type', models.CharField(max_length=3)),
                ('id_number_or_shelfmark', models.CharField(blank=True, max_length=500, null=True)),
                ('printed_edition_details', models.TextField(blank=True, null=True)),
                ('manifestation_notes', models.TextField(blank=True, null=True)),
                ('image_filenames', models.TextField(blank=True, null=True)),
                ('upload_name', models.CharField(blank=True, max_length=254, null=True)),
                ('_id', models.CharField(blank=True, max_length=32, null=True)),
                ('iwork', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='uploader.cofkcollectwork')),
                ('repository', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='uploader.cofkcollectinstitution')),
                ('union_manifestation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='manifestation.cofkunionmanifestation')),
                ('upload', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploader.cofkcollectupload')),
            ],
            options={
                'db_table': 'cofk_collect_manifestation',
                'unique_together': {('upload', 'iwork_id', 'manifestation_id')},
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
                ('upload', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='uploader.cofkcollectupload')),
            ],
            options={
                'db_table': 'cofk_collect_location_resource',
                'unique_together': {('upload', 'resource_id')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='cofkcollectlocation',
            unique_together={('upload', 'location_id')},
        ),
        migrations.CreateModel(
            name='CofkCollectLanguageOfWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_of_work_id', models.IntegerField()),
                ('_id', models.CharField(blank=True, max_length=32, null=True)),
                ('iwork', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='uploader.cofkcollectwork')),
                ('language_code', models.ForeignKey(db_column='language_code', on_delete=django.db.models.deletion.DO_NOTHING, to='core.iso639languagecode')),
                ('upload', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploader.cofkcollectupload')),
            ],
            options={
                'db_table': 'cofk_collect_language_of_work',
                'unique_together': {('upload', 'iwork_id', 'language_of_work_id')},
            },
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
        migrations.AlterUniqueTogether(
            name='cofkcollectdestinationofwork',
            unique_together={('upload', 'iwork_id', 'destination_id')},
        ),
        migrations.CreateModel(
            name='CofkCollectAuthorOfWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_id', models.IntegerField()),
                ('notes_on_author', models.TextField(blank=True, null=True)),
                ('_id', models.CharField(blank=True, max_length=32, null=True)),
                ('iperson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploader.cofkcollectperson')),
                ('iwork', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploader.cofkcollectwork')),
                ('upload', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploader.cofkcollectupload')),
            ],
            options={
                'db_table': 'cofk_collect_author_of_work',
                'unique_together': {('upload', 'iwork_id', 'author_id')},
            },
        ),
        migrations.CreateModel(
            name='CofkCollectAddresseeOfWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addressee_id', models.IntegerField()),
                ('notes_on_addressee', models.TextField(blank=True, null=True)),
                ('_id', models.CharField(blank=True, max_length=32, null=True)),
                ('iperson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploader.cofkcollectperson')),
                ('iwork', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploader.cofkcollectwork')),
                ('upload', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploader.cofkcollectupload')),
            ],
            options={
                'db_table': 'cofk_collect_addressee_of_work',
                'unique_together': {('upload', 'iwork_id', 'addressee_id')},
            },
        ),
    ]
