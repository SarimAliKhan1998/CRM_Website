from django import forms
from .models import Lead, Agent

class LeadModelForm(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        self.request = kwargs.pop('request')
        super(LeadModelForm, self).__init__(*args, **kwargs)

        self.fields['agent'] = forms.ModelChoiceField(
                queryset= Agent.objects.filter(organisation = self.request.user.userprofile)
            )

        self.fields['agent'].required = False


    class Meta :
        model = Lead
        
        fields = (
            "first_name",
            "last_name",
            "age",
            "agent",
        )

    # def clean_agent(self):
    #     return self.cleaned_data['agent'] or None


class LeadForm (forms.Form):

    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)