# Generated by Django 4.1.3 on 2022-11-24 10:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0018_alter_client_createdat_alter_project_createdat"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="createdat",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2022, 11, 24, 10, 56, 28, 795030, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="createdat",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2022, 11, 24, 10, 56, 28, 795030, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="users",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app1.users"
            ),
        ),
    ]
