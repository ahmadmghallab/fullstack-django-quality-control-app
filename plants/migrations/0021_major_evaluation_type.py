# Generated by Django 2.0.6 on 2018-07-07 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0020_evaluationtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='major',
            name='evaluation_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='major_evaluation_type', to='plants.EvaluationType'),
        ),
    ]
