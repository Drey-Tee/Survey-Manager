from django.db import models
from django.db.models.functions import Length
models.CharField.register_lookup(Length)


# Create your models here.
class SurveyParticipant(models.Model):
    name = models.CharField(max_length=64)
    slug = models.CharField(default='', max_length=64)


class Surveys(models.Model):
    survey_id = models.IntegerField()
    survey_name = models.CharField(max_length=64)
    # question = models.CharField(max_length = 400)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "survey"


class Questions(models.Model):
    survey_id = models.ForeignKey(Surveys, default=1, verbose_name="Survey", on_delete=models.SET_DEFAULT)
    question = models.TextField(max_length = 64)
    option_one = models.CharField(max_length=30)
    option_two = models.CharField(max_length=30)
    option_three = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "questions"


class Responses(models.Model):
    survey_id = models.ForeignKey(Surveys, default=1, verbose_name="Survey", on_delete=models.SET_DEFAULT)
    question_id = models.IntegerField()
    response =  models.TextField(max_length = 64)
    user_name =  models.TextField(max_length = 64)
    submitted_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "responses"


