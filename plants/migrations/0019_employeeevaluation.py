# Generated by Django 2.0.6 on 2018-07-07 09:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0018_auto_20180702_1318'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeEvaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('evaluation_score', models.IntegerField()),
                ('criteria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_evaluation_criteria', to='plants.Criteria')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_evaluation_employee_name', to='plants.Employee')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_evaluation_place', to='plants.Place')),
            ],
        ),
    ]
