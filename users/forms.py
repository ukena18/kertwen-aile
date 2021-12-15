from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# register form inherited from userceationform
class UserRegisterForm(UserCreationForm):
    # add an email to the form
    email = forms.EmailField()

    class Meta:
        # get the User model
        model = User
        # specify the fields
        fields = ['username', 'email', 'password1', 'password2']


# update form
class UserUpdateForm(forms.ModelForm):
    # add an email to the form
    email = forms.EmailField()

    class Meta:
        # get the User model
        model = User
        # specify the fields
        fields = ["username", 'email']

#
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        # get the profile model
        model = Profile
        # specify the fields
        fields = ['image']
