# Generated by Django 3.1.7 on 2021-10-06 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_model2_id2'),
    ]

    operations = [
        migrations.RunSQL(sql="UPDATE data_model2 SET id2 = gen_random_uuid();", reverse_sql=migrations.RunSQL.noop)
    ]