# Generated by Django 5.0.4 on 2024-05-05 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handle_units', '0002_case_affidavit_vakalat_date_case_case_type_case_cnr_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team_member',
            name='id',
        ),
        migrations.AlterField(
            model_name='team_member',
            name='member_id',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]