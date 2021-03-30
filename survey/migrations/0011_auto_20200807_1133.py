# Generated by Django 2.2.2 on 2020-08-07 11:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0010_responses'),
    ]

    operations = [
        migrations.CreateModel(
            name='Surveys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survey_id', models.IntegerField()),
                ('survey_name', models.CharField(max_length=64)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'survey',
            },
        ),
        migrations.AddField(
            model_name='questions',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questions',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='responses',
            name='submitted_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='responses',
            name='survey_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='survey.Surveys', verbose_name='Survey'),
        ),
        migrations.DeleteModel(
            name='SurveyQuestions',
        ),
        migrations.AddField(
            model_name='questions',
            name='survey_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='survey.Surveys', verbose_name='Survey'),
        ),
    ]