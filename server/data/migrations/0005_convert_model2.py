# Generated by Django 3.1.7 on 2021-10-06 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_delete_model2'),
    ]

    operations = [
        migrations.RunSQL(sql="CREATE TABLE data_model2 AS SELECT gen_random_uuid() as id, time, user_id, steps from data_model2_backup;", reverse_sql=migrations.RunSQL.noop),
    ]
