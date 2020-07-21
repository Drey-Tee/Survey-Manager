from django.db import models
from django.db.models.functions import Length


# Create your models here.
models.CharField.register_lookup(Length)


class Survey(models.Model):
    """Table schema to store articles."""
    name = models.CharField(max_length=64)
    survey_participants = models.ForeignKey('survey.SurveyParticipant', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length = 100)
    slug = models.CharField(default='', max_length=64)

    def __str__(self):
        return '%s' % self.name

class SurveyParticipant(models.Model):
    """Table schema to store auhtors."""
    name = models.CharField(max_length=64)
    slug = models.CharField(default='', max_length=64)

    def __str__(self):
        return '%s' % self.name