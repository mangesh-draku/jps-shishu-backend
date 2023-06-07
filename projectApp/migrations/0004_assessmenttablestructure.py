# Generated by Django 4.1.7 on 2023-06-05 10:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0003_remove_studenttablestructure_admission_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssessmentTableStructure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=255, null=True)),
                ('standard', models.CharField(default=None, max_length=255, null=True)),
                ('subject', models.CharField(default=None, max_length=255, null=True)),
                ('teacher_name', models.CharField(default=None, max_length=255, null=True)),
                ('question_type', models.CharField(default=None, max_length=255, null=True)),
                ('date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('marks', models.IntegerField(blank=True, default=None, null=True)),
            ],
            options={
                'db_table': 'assessment_table_structure',
            },
        ),
    ]