# Generated by Django 2.0.6 on 2018-07-15 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0028_remove_ticketevaluation_major'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticketevaluation',
            name='criteria',
        ),
        migrations.RemoveField(
            model_name='ticketevaluation',
            name='date',
        ),
        migrations.RemoveField(
            model_name='ticketevaluation',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='ticketevaluation',
            name='place',
        ),
        migrations.RemoveField(
            model_name='ticketevaluation',
            name='ticket_number',
        ),
        migrations.RemoveField(
            model_name='ticketevaluation',
            name='yes_or_no',
        ),
    ]
