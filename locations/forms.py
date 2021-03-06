from django import forms
from models import Location

class LocationForm(forms.ModelForm):

    class Meta:
    	model = Location
        fields = ('name', 'type', 'parent', 'overlapswith')

class LocationSelectForm(forms.ModelForm):

	class Meta:
		model = Location
		fields = ('name',)