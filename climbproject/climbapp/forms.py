from django import forms
#from django.core import validators
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class ClimbForm(forms.Form):
    climb = forms.CharField(
        # validators=[validators.validate_slug],
        label='Climb', max_length=240
        )
#
# class RegistrationForm(UserCreationForm):
#     email = forms.EmailField(
#         label="Email",
#         required=True
#         )
#      class Meta:
#         model = User
#         fields = ("username", "email",
#             "password1", "password2")
#      def save(self, commit=True):
#         user=super(RegistrationForm,self).save(commit=False)
#         user.email=self.cleaned_data["email"]
#         if commit:
#             user.save()
#         return user
