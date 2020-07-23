from django import forms
from .models import Survey

class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        # fields = ('sp_id', 'survey_name', 'content', 'slug')
        fields = "__all__"
