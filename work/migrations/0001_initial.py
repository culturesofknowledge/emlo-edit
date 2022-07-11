# Generated by Django 4.0.6 on 2022-07-07 13:43

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('uploader', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CofkUnionWork',
            fields=[
                ('work_id', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('date_of_work_as_marked', models.CharField(max_length=250)),
                ('original_calendar', models.CharField(default='', max_length=2)),
                ('date_of_work_std', models.CharField(max_length=12)),
                ('date_of_work_std_gregorian', models.CharField(max_length=12)),
                ('date_of_work_std_year', models.IntegerField(null=True)),
                ('date_of_work_std_month', models.IntegerField(null=True)),
                ('date_of_work_std_day', models.IntegerField(null=True)),
                ('date_of_work2_std_year', models.IntegerField(null=True)),
                ('date_of_work2_std_month', models.IntegerField(null=True)),
                ('date_of_work2_std_day', models.IntegerField(null=True)),
                ('date_of_work_std_is_range', models.BooleanField(default=False)),
                ('date_of_work_inferred', models.BooleanField(default=False)),
                ('date_of_work_uncertain', models.BooleanField(default=False)),
                ('date_of_work_approx', models.BooleanField(default=False)),
                ('authors_as_marked', models.TextField(null=True)),
                ('addressees_as_marked', models.TextField(null=True)),
                ('authors_inferred', models.BooleanField(default=False)),
                ('authors_uncertain', models.BooleanField(default=False)),
                ('addressees_inferred', models.BooleanField(default=False)),
                ('addressees_uncertain', models.BooleanField(default=False)),
                ('destination_as_marked', models.TextField(null=True)),
                ('origin_as_marked', models.TextField(null=True)),
                ('destination_inferred', models.BooleanField(default=False)),
                ('destination_uncertain', models.BooleanField(default=False)),
                ('origin_inferred', models.BooleanField(default=False)),
                ('origin_uncertain', models.BooleanField(default=False)),
                ('abstract', models.TextField(null=True)),
                ('keywords', models.TextField(null=True)),
                ('language_of_work', models.CharField(max_length=255)),
                ('work_is_translation', models.BooleanField(default=False)),
                ('incipit', models.TextField(null=True)),
                ('explicit', models.TextField(null=True)),
                ('ps', models.TextField(null=True)),
                ('accession_code', models.CharField(max_length=1000)),
                ('work_to_be_deleted', models.BooleanField(default=False)),
                ('iwork_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('editors_notes', models.TextField(null=True)),
                ('edit_status', models.CharField(default='', max_length=3)),
                ('relevant_to_cofk', models.CharField(default='Y', max_length=3)),
                ('creation_timestamp', models.DateTimeField(auto_now=True)),
                ('change_timestamp', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('original_catalogue', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='uploader.cofklookupcatalogue')),
            ],
        ),
        migrations.CreateModel(
            name='CofkUnionLanguageOfWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.CharField(max_length=100)),
                ('language_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploader.iso639languagecode')),
                ('work_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='work.cofkunionwork')),
            ],
        ),
        migrations.CreateModel(
            name='CofkCollectWorkResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_name', models.TextField(default='')),
                ('resource_details', models.TextField(default='')),
                ('resource_url', models.TextField(default='')),
                ('_id', models.CharField(max_length=32)),
                ('upload_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploader.cofkcollectupload')),
            ],
        ),
        migrations.CreateModel(
            name='CofkCollectWork',
            fields=[
                ('iwork_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_of_work_as_marked', models.CharField(max_length=250)),
                ('original_calendar', models.CharField(default='', max_length=2)),
                ('date_of_work_std_year', models.IntegerField(null=True)),
                ('date_of_work_std_month', models.IntegerField(null=True)),
                ('date_of_work_std_day', models.IntegerField(null=True)),
                ('date_of_work2_std_year', models.IntegerField(null=True)),
                ('date_of_work2_std_month', models.IntegerField(null=True)),
                ('date_of_work2_std_day', models.IntegerField(null=True)),
                ('date_of_work_std_is_range', models.BooleanField(default=False, null=True)),
                ('date_of_work_inferred', models.BooleanField(default=False, null=True)),
                ('date_of_work_uncertain', models.BooleanField(default=False, null=True)),
                ('date_of_work_approx', models.BooleanField(default=False, null=True)),
                ('notes_on_date_of_work', models.TextField(null=True)),
                ('authors_as_marked', models.TextField(null=True)),
                ('authors_inferred', models.BooleanField(default=False, null=True)),
                ('authors_uncertain', models.BooleanField(default=False, null=True)),
                ('notes_on_authors', models.TextField(null=True)),
                ('addressees_as_marked', models.TextField(null=True)),
                ('addressees_inferred', models.BooleanField(default=False, null=True)),
                ('addressees_uncertain', models.BooleanField(default=False, null=True)),
                ('notes_on_addressees', models.TextField(null=True)),
                ('destination_id', models.IntegerField(null=True)),
                ('destination_as_marked', models.TextField(null=True)),
                ('destination_inferred', models.BooleanField(default=False, null=True)),
                ('destination_uncertain', models.BooleanField(default=False, null=True)),
                ('origin_id', models.IntegerField(null=True)),
                ('origin_as_marked', models.TextField(null=True)),
                ('origin_inferred', models.BooleanField(default=False, null=True)),
                ('origin_uncertain', models.BooleanField(default=False, null=True)),
                ('abstract', models.TextField(null=True)),
                ('keywords', models.TextField(null=True)),
                ('language_of_work', models.CharField(max_length=255)),
                ('incipit', models.TextField(null=True)),
                ('excipit', models.TextField(null=True)),
                ('accession_code', models.CharField(max_length=250)),
                ('notes_on_letter', models.TextField(null=True)),
                ('notes_on_people_mentioned', models.TextField(null=True)),
                ('editors_notes', models.TextField(null=True)),
                ('_id', models.CharField(max_length=32)),
                ('date_of_work2_approx', models.BooleanField(default=False, null=True)),
                ('date_of_work2_inferred', models.BooleanField(default=False, null=True)),
                ('date_of_work2_uncertain', models.BooleanField(default=False, null=True)),
                ('mentioned_as_marked', models.TextField(null=True)),
                ('mentioned_inferred', models.BooleanField(default=False, null=True)),
                ('mentioned_uncertain', models.BooleanField(default=False, null=True)),
                ('notes_on_destination', models.TextField(null=True)),
                ('notes_on_origin', models.TextField(null=True)),
                ('notes_on_place_mentioned', models.TextField(null=True)),
                ('place_mentioned_as_marked', models.TextField(null=True)),
                ('place_mentioned_inferred', models.BooleanField(default=False, null=True)),
                ('place_mentioned_uncertain', models.BooleanField(default=False, null=True)),
                ('upload_name', models.CharField(max_length=254)),
                ('explicit', models.TextField(null=True)),
                ('union_iwork_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='work.cofkunionwork')),
                ('upload_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploader.cofkcollectupload')),
                ('upload_status', models.ForeignKey(default='1', on_delete=django.db.models.deletion.DO_NOTHING, to='uploader.cofkcollectstatus')),
            ],
        ),
        migrations.CreateModel(
            name='CofkCollectSubjectOfWork',
            fields=[
                ('subject_of_work_id', models.AutoField(primary_key=True, serialize=False)),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploader.cofkunionsubject')),
                ('upload_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploader.cofkcollectupload')),
            ],
        ),
        migrations.CreateModel(
            name='CofkCollectPlaceMentionedInWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_id', models.IntegerField()),
                ('notes_on_place_mentioned', models.TextField(null=True)),
                ('_id', models.CharField(max_length=32)),
                ('upload_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploader.cofkcollectupload')),
            ],
        ),
        migrations.CreateModel(
            name='CofkCollectPersonMentionedInWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iperson_id', models.IntegerField()),
                ('notes_on_person_mentioned', models.TextField(null=True)),
                ('_id', models.CharField(max_length=32)),
                ('upload_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploader.cofkcollectupload')),
            ],
        ),
        migrations.CreateModel(
            name='CofkCollectOriginOfWork',
            fields=[
                ('origin_id', models.AutoField(primary_key=True, serialize=False)),
                ('location_id', models.IntegerField()),
                ('notes_on_origin', models.TextField(null=True)),
                ('_id', models.CharField(max_length=32)),
                ('upload_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploader.cofkcollectupload')),
            ],
        ),
        migrations.CreateModel(
            name='CofkCollectLanguageOfWork',
            fields=[
                ('language_of_work_id', models.AutoField(primary_key=True, serialize=False)),
                ('_id', models.CharField(max_length=32)),
                ('language_code', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='uploader.iso639languagecode')),
                ('upload_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploader.cofkcollectupload')),
            ],
        ),
        migrations.CreateModel(
            name='CofkCollectDestinationOfWork',
            fields=[
                ('destination_id', models.AutoField(primary_key=True, serialize=False)),
                ('location_id', models.IntegerField()),
                ('notes_on_destination', models.TextField(null=True)),
                ('_id', models.CharField(max_length=32)),
                ('upload_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploader.cofkcollectupload')),
            ],
        ),
        migrations.CreateModel(
            name='CofkCollectAuthorOfWork',
            fields=[
                ('author_id', models.AutoField(primary_key=True, serialize=False)),
                ('iperson_id', models.IntegerField()),
                ('notes_on_author', models.TextField(null=True)),
                ('_id', models.CharField(max_length=32)),
                ('upload_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploader.cofkcollectupload')),
            ],
        ),
        migrations.CreateModel(
            name='CofkCollectAddresseeOfWork',
            fields=[
                ('addressee_id', models.AutoField(primary_key=True, serialize=False)),
                ('iperson_id', models.IntegerField()),
                ('notes_on_addressee', models.TextField(null=True)),
                ('_id', models.CharField(max_length=32)),
                ('upload_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploader.cofkcollectupload')),
            ],
        ),
    ]
