# Generated by Django 4.1.3 on 2022-11-23 20:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_alter_client_createdat_alter_project_createdat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='createdat',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 20, 49, 4, 286692, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='createdat',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 20, 49, 4, 286692, tzinfo=datetime.timezone.utc)),
        ),
    ]