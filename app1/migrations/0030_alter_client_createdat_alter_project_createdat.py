# Generated by Django 4.1.3 on 2022-11-24 12:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0029_remove_project_users_alter_client_createdat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='createdat',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 24, 12, 55, 7, 207300, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='createdat',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 24, 12, 55, 7, 207300, tzinfo=datetime.timezone.utc)),
        ),
    ]