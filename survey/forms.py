from django import forms
from .models import  SurveyQuestions, Questions


class QuestionForm(forms.ModelForm):
    class Meta:
        model = SurveyQuestions
        fields = ('survey_id', 'survey_name')
        # fields = "__all__"


class CreateQuestionForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ('question', 'option_one', 'option_two', 'option_three')