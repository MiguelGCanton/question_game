from django import forms
from .models import Team

class Team_form(forms.Form):
	
	class Meta:
		model = Team
        name = forms.CharField(label='Your team name')

        fields = ('title', 'text',)
