# Generated by Django 4.0.6 on 2024-09-20 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0010_alter_cofkunionlanguageofwork_language_code_and_more'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='cofkunionwork',
            index=models.Index(fields=['iwork_id'], name='cofk_union__iwork_i_98a3a4_idx'),
        ),
    ]