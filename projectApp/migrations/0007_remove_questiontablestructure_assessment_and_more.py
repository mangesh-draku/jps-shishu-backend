# Generated by Django 4.1.7 on 2023-06-05 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0006_remove_assessmenttablestructure_questions_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questiontablestructure',
            name='assessment',
        ),
        migrations.AddField(
            model_name='assessmenttablestructure',
            name='questions',
            field=models.ForeignKey(db_column='question_id', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assessment', to='projectApp.questiontablestructure'),
        ),
    ]