# Generated by Django 3.2.15 on 2022-11-07 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_task_deadline'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='creator',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='creator',
            new_name='user',
        ),
    ]
