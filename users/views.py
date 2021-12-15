# redirect after successful post request
from django.shortcuts import render, redirect
# django built in UserCreation form , it doesn't have email, so we used our custom form
from django.contrib.auth.forms import UserCreationForm
# flash messages using in the templates send from views
from django.contrib import messages
# The Forms i created in the forms.py
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
# authenticated for func view
from django.contrib.auth.decorators import login_required

# for register
def register(request):
    # our custom register form   with email field
    form = UserRegisterForm()

    # if it is post request
    if request.method == 'POST':
        # get the form with all the entered values
        form = UserRegisterForm(request.POST)
        # we inherited from user-creation-form  so django know once we save it is creating user
        if form.is_valid():
            # save the user with all credential
            form.save()
            # get the username for flash message for visual approve that we save the user
            username = form.cleaned_data['username']
            messages.success(request, f"Your Account has been created")
            # redirect it
            return redirect('login')
    # if it is get request render template with empty form
    return render(request, 'users/register.html', {"form": form})

# if user is not authenticated send them to login url = reverse(login) same thing
@login_required(login_url="login")
def profile(request):
    # to fill the update form with current user infos
    u_data = {
        "username":request.user.username,
        "email":request.user.email
    }
    p_data = {
        "image":request.user.profile.image
    }
    # pass the infos to forms
    u_form = UserUpdateForm(initial=u_data)
    p_form = ProfileUpdateForm(initial=p_data)

    context = {
        "u_form": u_form,
        "p_form": p_form
    }
    # if it is post request
    if request.method == 'POST':
        # prefill the photo form
        # request.FILES is for photos/videos , instance = filled up old data
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        # instance is current data for user request.user and for Profile is request.user.profile
        u_form = UserUpdateForm(request.POST, instance=request.user)
        # then save it   is_valid is built in func
        if p_form.is_valid() and u_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your Profile has been updated!')
            return redirect('profile')
    return render(request, 'users/profile.html', context)
