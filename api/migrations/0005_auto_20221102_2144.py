# Generated by Django 3.2.15 on 2022-11-02 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20221008_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='member_count',
        ),
        migrations.RemoveField(
            model_name='task',
            name='is_done',
        ),
    ]