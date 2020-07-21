from django.forms import ModelForm, TextInput, Select
from app.models import SurveyParticipant


class SurveyParticpantForm(ModelForm):
    content = forms.ModelChoiceField(
        queryset=Survey.objects.all(),
        widget=Select(attrs={'class': 'content'}),
    )

    class Meta:
        model = SP
        fields = ('name','slug')
        widgets = {
            'name': TextInput(attrs={'class': 'name'})
        }