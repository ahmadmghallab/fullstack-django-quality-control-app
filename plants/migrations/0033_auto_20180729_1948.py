# Generated by Django 2.0.6 on 2018-07-29 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0032_auto_20180729_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='evaluation_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_evaluation_type', to='plants.EvaluationType'),
        ),
    ]
