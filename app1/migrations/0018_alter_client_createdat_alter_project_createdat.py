# Generated by Django 4.1.3 on 2022-11-24 10:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0017_alter_client_createdat_alter_project_createdat"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="createdat",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2022, 11, 24, 10, 55, 31, 406175, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="createdat",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2022, 11, 24, 10, 55, 31, 406175, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
