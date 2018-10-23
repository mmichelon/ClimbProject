from django import forms
from django.core import validators

class ClimbForm(forms.Form):
    climb = forms.CharField(
        # validators=[validators.validate_slug],
        label='Climb', max_length=240
        )
