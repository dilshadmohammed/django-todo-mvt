# Generated by Django 5.0.4 on 2024-05-06 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_rename_status_todo_completed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='expiry',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
