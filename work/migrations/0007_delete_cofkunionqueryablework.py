# Generated by Django 4.0.6 on 2023-05-15 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0006_remove_cofkunionwork_language_of_work_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CofkUnionQueryableWork',
        ),
    ]
