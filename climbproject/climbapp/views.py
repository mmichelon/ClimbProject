from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

#User Authentication
from django.contrib.auth import logout
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Create your views here.
#from django.http import HttpResponse
from . import models
from . import forms

@login_required
def index(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form_instance = forms.ClimbForm(request.POST)
        if form_instance.is_valid():

            # climb = models.ClimbModel(
            #     climb = form_instance.cleaned_data["climb"]
            # )
            # climb.save()
            # form_instance=forms.ClimbForm()

            if request.user.is_authenticated:
                climb = models.ClimbModel(
                    climb = form_instance.cleaned_data["climb"],
                    author = request.user
                )
                climb.save()
                form_instance = forms.ClimbForm()

    else:
        form_instance = forms.ClimbForm()
    climbs = models.ClimbModel.objects.all()
    context = {
        "title":"Climb to the Max",
        "climbs":climbs,
        "form_instance":form_instance
        }
    return render(request, "index.html", context=context)

def logout_view(request):
    logout(request)
    return redirect("/login/")

def register(request):
    if request.method == 'POST':
        registration_form = forms.RegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save(commit=True)
            return redirect("/")
    else:
        registration_form = forms.RegistrationForm()
    context = {
        "form":registration_form
        }
    return render(request, "registration/register.html", context=context)

def account(request):
    context = {
        "title": "Account",
        }
    return render(request, "registration/account.html", context=context)

def information(request):
    context = {
        "title": "Climbing Information",
        }
    return render(request, "information/information.html", context=context)

def indoor(request):
    context = {
        "title": "Indoor Climbing",
        }
    return render(request, "information/indoor.html", context=context)

def outdoor(request):
    context = {
        "title": "Outdoor Climbing",
        }
    return render(request, "information/outdoor.html", context=context)

def equipment(request):
    context = {
        "title": "Equipment",
        }
    return render(request, "information/equipment.html", context=context)

def rest_climb(request):
    if not request.user.is_authenticated:
        return JsonResponse({"climbs":[]})
    if request.method == 'GET':
        climbs = models.ClimbModel.objects.all()
        list_of_climbs = []
        for item in climbs:
            list_of_climbs += [{
                "climb":item.climb,
                "author":item.author.username,
                "id":item.id
            }]
        # return JsonResponse(list_of_climbs,safe=False)
        return JsonResponse({"climbs": list_of_climbs})
    else:
        return HttpResponse("Invalid HTTP Method")
