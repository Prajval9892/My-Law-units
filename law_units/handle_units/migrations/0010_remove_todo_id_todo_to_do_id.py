# Generated by Django 5.0.4 on 2024-05-07 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handle_units', '0009_todo_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='id',
        ),
        migrations.AddField(
            model_name='todo',
            name='to_do_id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
