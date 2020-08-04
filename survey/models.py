from django.db import models
from django.db.models.functions import Length
models.CharField.register_lookup(Length)


# Create your models here.
class SurveyParticipant(models.Model):
    name = models.CharField(max_length=64)
    slug = models.CharField(default='', max_length=64)


class SurveyQuestions(models.Model):
    survey_id = models.IntegerField()
    survey_name = models.CharField(max_length=64)
    question = models.CharField(max_length = 400)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "survey_questions"


class Questions(models.Model):
    question = models.TextField()
    option_one = models.CharField(max_length=30)
    option_two = models.CharField(max_length=30)
    option_three = models.CharField(max_length=30)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)

    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count

    class Meta:
        db_table = "questions"

