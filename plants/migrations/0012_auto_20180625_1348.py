# Generated by Django 2.0.6 on 2018-06-25 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0011_auto_20180625_1240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='en_name',
        ),
        migrations.AlterField(
            model_name='criteria',
            name='major',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='criteria_department', to='plants.Major'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='en_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='major',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_department', to='plants.Major'),
        ),
        migrations.AlterField(
            model_name='yesornoresult',
            name='major',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='result_department', to='plants.Major'),
        ),
    ]
