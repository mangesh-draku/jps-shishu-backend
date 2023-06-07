# Generated by Django 4.1.7 on 2023-06-05 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0004_assessmenttablestructure'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessmenttablestructure',
            name='date_time',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='assessmenttablestructure',
            name='end_time',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='assessmenttablestructure',
            name='grade',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='assessmenttablestructure',
            name='int_ext_type',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='assessmenttablestructure',
            name='questions',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projectApp.questiontablestructure'),
        ),
        migrations.AddField(
            model_name='assessmenttablestructure',
            name='subject_id',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='assessmenttablestructure',
            name='test_category',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='assessmenttablestructure',
            name='test_duration',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='assessmenttablestructure',
            name='test_type',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='assessmenttablestructure',
            name='title',
            field=models.CharField(default='Assessment', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='assessmenttablestructure',
            name='topic_id',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='questiontablestructure',
            name='mark',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]