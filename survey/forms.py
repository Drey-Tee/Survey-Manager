from django import forms
from .models import  Surveys, Questions


class SurveyForm(forms.ModelForm):
    class Meta:
        model = Surveys
        fields = ('survey_name','survey_id')
        # fields = "__all__"


class CreateQuestionForm(forms.ModelForm):
    option_one = forms.CharField(required=True)
    option_two = forms.CharField(required=True)
    option_three = forms.CharField(required=True)

    class Meta:
        model = Questions
        fields = ('survey_id','question', 'option_one', 'option_two', 'option_three')