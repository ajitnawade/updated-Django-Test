# Generated by Django 4.1.3 on 2022-11-23 14:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0007_rename_cname_client_client_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="createdat",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2022, 11, 23, 14, 23, 7, 445776, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="createdat",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2022, 11, 23, 14, 23, 7, 445776, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
