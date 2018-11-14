from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class ClimbForm(forms.Form):

    climb = forms.CharField(
        label='Climb', max_length=240
        )
    difficulty = forms.CharField(
        label='Difficulty', max_length=10
    )

    CHOICES=[('1','Indoor'),
         ('2','Outdoor')]
    in_or_out = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())


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
