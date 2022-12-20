# Generated by Django 4.0.6 on 2022-12-20 12:27

import core.helper.model_utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CofkUnionPublication',
            fields=[
                ('publication_id', models.AutoField(primary_key=True, serialize=False)),
                ('publication_details', models.TextField()),
                ('change_timestamp', models.DateTimeField(blank=True, default=core.helper.model_utils.default_current_timestamp, null=True)),
                ('change_user', models.CharField(max_length=50)),
                ('abbrev', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'cofk_union_publication',
            },
        ),
    ]
