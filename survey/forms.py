from django import forms
from .models import  SurveyQuestions, Questions


class QuestionForm(forms.ModelForm):
    class Meta:
        model = SurveyQuestions
        fields = ('survey_name','survey_id')
        # fields = "__all__"


class CreateQuestionForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ('question', 'question_type','option_one', 'option_two', 'option_three')