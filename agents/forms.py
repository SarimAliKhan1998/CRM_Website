from django import forms
from django import forms
# from leads.models import Agent
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

user = get_user_model()


class AgentModelForm(forms.ModelForm):
    class Meta:
        model = user
        fields = (
            'email',
            'username',
            'first_name',
            'last_name',
        )