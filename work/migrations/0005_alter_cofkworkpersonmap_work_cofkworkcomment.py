# Generated by Django 4.0.6 on 2022-10-04 10:58

import core.helper.model_utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('work', '0004_cofkworkpersonmap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cofkworkpersonmap',
            name='work',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.cofkunionwork'),
        ),
        migrations.CreateModel(
            name='CofkWorkComment',
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
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.cofkunionwork')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, core.helper.model_utils.RecordTracker),
        ),
    ]