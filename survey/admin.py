from django.contrib import admin
from .models import SurveyParticipant,Surveys,Questions, Responses

# Register your models here.
# admin.site.register(Survey)
admin.site.register(SurveyParticipant)
admin.site.register(Surveys)
admin.site.register(Questions)
admin.site.register(Responses)