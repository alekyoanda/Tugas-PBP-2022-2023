# Generated by Django 4.1 on 2022-10-10 19:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todolist", "0005_alter_task_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2022, 10, 10, 19, 33, 53, 555481, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
