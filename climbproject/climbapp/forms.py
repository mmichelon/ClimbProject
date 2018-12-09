from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class ClimbForm(forms.Form):
    climb = forms.CharField(
        label='Name/Location', max_length=240
        )
    difficulty = forms.CharField(
        label='Difficulty', max_length=10
    )

    CHOICES = ((0, 'Indoor'), (1, 'Outdoor'))
    outdoor_bool = forms.TypedChoiceField(
        choices=CHOICES, widget=forms.RadioSelect, coerce=int
        )

    climb_notes = forms.CharField(
        label='Notes:', max_length=240, required=False
        )

class searchForm(forms.Form):
    climbType = forms.CharField(
        label="Find a climb", max_length=50
    )

class CommentForm(forms.Form):
    comment = forms.CharField(
        label='Comment', max_length=240
        )

#get new user
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True
        )

    class Meta:
        model = User
        fields = ("username", "email",
                "password1", "password2")

    def save(self, commit=True):
        user = super(RegistrationForm,self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
