from django import forms
from .models import user

class userform(forms.ModelForm):
	class Meta:
		model=user
		fields=["name","username","password","confirm_pass"]