from django.contrib import admin
from .models import SurveyParticipant,SurveyQuestions,Questions

# Register your models here.
# admin.site.register(Survey)
admin.site.register(SurveyParticipant)
admin.site.register(SurveyQuestions)
admin.site.register(Questions)