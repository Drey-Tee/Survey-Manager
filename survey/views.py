from django.shortcuts import render
from .models import Survey, SurveyParticipant


# Create your views here.
def frontend(request):
    """Vue.js will take care of everything else."""
    surveys = Survey.objects.all()
    surveyparticipants = SurveyParticipant.objects.all()

    data = {
        'surveys': surveys,
        'surveyparticipants': surveyparticipants,
    }

    return render(request, 'survey/templates.html', data)