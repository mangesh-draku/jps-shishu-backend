# Generated by Django 4.1.7 on 2023-06-05 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0007_remove_questiontablestructure_assessment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assessmenttablestructure',
            name='questions',
        ),
        migrations.AddField(
            model_name='questiontablestructure',
            name='assessment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='projectApp.assessmenttablestructure'),
        ),
    ]