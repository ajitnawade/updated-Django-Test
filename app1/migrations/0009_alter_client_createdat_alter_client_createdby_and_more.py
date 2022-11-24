# Generated by Django 4.1.3 on 2022-11-23 18:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_alter_client_createdat_alter_project_createdat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='createdat',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 18, 48, 57, 330284, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='client',
            name='createdby',
            field=models.CharField(default='admin', max_length=40),
        ),
        migrations.AlterField(
            model_name='project',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.client'),
        ),
        migrations.AlterField(
            model_name='project',
            name='createdat',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 18, 48, 57, 332130, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='createdby',
            field=models.CharField(max_length=40),
        ),
    ]
