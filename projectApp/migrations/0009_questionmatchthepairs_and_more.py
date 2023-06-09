# Generated by Django 4.1.7 on 2023-06-07 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0008_remove_assessmenttablestructure_questions_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionMatchThePairs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option1', models.TextField(blank=True, max_length=500, null=True)),
                ('option2', models.TextField(blank=True, max_length=500, null=True)),
                ('option3', models.TextField(blank=True, max_length=500, null=True)),
                ('option4', models.TextField(blank=True, max_length=500, null=True)),
                ('option5', models.TextField(blank=True, max_length=500, null=True)),
                ('option6', models.TextField(blank=True, max_length=500, null=True)),
                ('question', models.TextField(blank=True, max_length=500, null=True)),
                ('option_count', models.TextField(blank=True, max_length=500, null=True)),
                ('mark', models.IntegerField(blank=True, default=None, null=True)),
                ('chapter_id', models.IntegerField(blank=True, default=None, null=True)),
                ('subject_id', models.IntegerField(blank=True, default=None, null=True)),
                ('answer', models.CharField(default=None, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionMultipleChoiceQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option1', models.TextField(blank=True, max_length=500, null=True)),
                ('option2', models.TextField(blank=True, max_length=500, null=True)),
                ('option3', models.TextField(blank=True, max_length=500, null=True)),
                ('option4', models.TextField(blank=True, max_length=500, null=True)),
                ('option5', models.TextField(blank=True, max_length=500, null=True)),
                ('option6', models.TextField(blank=True, max_length=500, null=True)),
                ('question', models.TextField(blank=True, max_length=500, null=True)),
                ('option_count', models.TextField(blank=True, max_length=500, null=True)),
                ('mark', models.IntegerField(blank=True, default=None, null=True)),
                ('chapter_id', models.IntegerField(blank=True, default=None, null=True)),
                ('subject_id', models.IntegerField(blank=True, default=None, null=True)),
                ('answer', models.CharField(default=None, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionSelectReleventPicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option1', models.TextField(blank=True, max_length=500, null=True)),
                ('option2', models.TextField(blank=True, max_length=500, null=True)),
                ('option3', models.TextField(blank=True, max_length=500, null=True)),
                ('option4', models.TextField(blank=True, max_length=500, null=True)),
                ('option5', models.TextField(blank=True, max_length=500, null=True)),
                ('option6', models.TextField(blank=True, max_length=500, null=True)),
                ('question', models.TextField(blank=True, max_length=500, null=True)),
                ('option_count', models.TextField(blank=True, max_length=500, null=True)),
                ('mark', models.IntegerField(blank=True, default=None, null=True)),
                ('chapter_id', models.IntegerField(blank=True, default=None, null=True)),
                ('subject_id', models.IntegerField(blank=True, default=None, null=True)),
                ('answer', models.CharField(default=None, max_length=255, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='questiontablestructure',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='questiontablestructure',
            name='answer_explanation',
        ),
        migrations.RemoveField(
            model_name='questiontablestructure',
            name='answer_explanation_images',
        ),
        migrations.RemoveField(
            model_name='questiontablestructure',
            name='chapter_id',
        ),
        migrations.RemoveField(
            model_name='questiontablestructure',
            name='default_weight_age',
        ),
        migrations.RemoveField(
            model_name='questiontablestructure',
            name='language_id',
        ),
        migrations.RemoveField(
            model_name='questiontablestructure',
            name='mark',
        ),
        migrations.RemoveField(
            model_name='questiontablestructure',
            name='objective_subjective_type',
        ),
        migrations.RemoveField(
            model_name='questiontablestructure',
            name='option1',
        ),
        migrations.RemoveField(
            model_name='questiontablestructure',
            name='option2',
        ),
        migrations.RemoveField(
            model_name='questiontablestructure',
            name='option3',
        ),
        migrations.RemoveField(
            model_name='questiontablestructure',
            name='option4',
        ),
        migrations.RemoveField(
            model_name='questiontablestructure',
            name='option5',
        ),
        migrations.RemoveField(
            model_name='questiontablestructure',
            name='option6',
        ),
        migrations.RemoveField(
            model_name='questiontablestructure',
            name='option_count',
        ),
        migrations.RemoveField(
            model_name='questiontablestructure',
            name='question',
        ),
        migrations.RemoveField(
            model_name='questiontablestructure',
            name='question_image',
        ),
        migrations.RemoveField(
            model_name='questiontablestructure',
            name='subject_id',
        ),
        migrations.AddField(
            model_name='questiontablestructure',
            name='match_the_pairs_question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='match_the_pairs_question', to='projectApp.questionmatchthepairs'),
        ),
        migrations.AddField(
            model_name='questiontablestructure',
            name='multiple_choice_question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='multiple_choice_question', to='projectApp.questionmultiplechoicequestions'),
        ),
        migrations.AddField(
            model_name='questiontablestructure',
            name='select_relevent_picture_question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='select_relevent_picture_question', to='projectApp.questionselectreleventpicture'),
        ),
    ]
