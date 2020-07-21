class ParticpantForm(ModelForm):
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