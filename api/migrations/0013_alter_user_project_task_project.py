# Generated by Django 3.2.15 on 2022-12-10 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_alter_user_project_task_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_project_task',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.project'),
        ),
    ]
