# Generated by Django 4.0.6 on 2023-03-06 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_cofklookupcatalogue_options_and_more'),
        ('work', '0005_alter_cofkunionqueryablework_work'),
    ]

    operations = [
        migrations.AddField(
            model_name='cofkunionwork',
            name='subjects',
            field=models.ManyToManyField(related_name='work', through='work.CofkWorkSubjectMap', to='core.cofkunionsubject'),
        ),
        migrations.AlterField(
            model_name='cofkunionwork',
            name='original_catalogue',
            field=models.ForeignKey(blank=True, db_column='original_catalogue', db_constraint=False, default='', on_delete=django.db.models.deletion.DO_NOTHING, related_name='work', to='core.cofklookupcatalogue', to_field='catalogue_code'),
        ),
    ]
