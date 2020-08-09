from django import forms

from .models import AudioFeed

class TextFileForm(forms.ModelForm):
	class Meta:
		model = AudioFeed
		fields = {'text'}