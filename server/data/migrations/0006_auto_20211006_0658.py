# Generated by Django 3.1.7 on 2021-10-06 06:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_convert_model2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model2',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
    ]
