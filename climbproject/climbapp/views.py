from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
#from django.http import HttpResponse
from . import models
from . import forms

# def index(request):
#     # return HttpResponse("Hello, world. You're at the polls index.")
#     if request.mehod == 'POST':
def index(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form_instance = forms.ClimbForm(request.POST)
        if form_instance.is_valid():
            climb = models.ClimbModel(
                climb=form_instance.cleaned_data["climb"]
            )
            climb.save()
            form_instance=forms.ClimbForm()
    else:
        form_instance = forms.ClimbForm()
    climbs = models.ClimbModel.objects.all()
    context = {
        "title":"Awesome",
        "climbs":climbs,
        "climbs":climbs,
        "form_instance":form_instance
        }
    return render(request, "index.html", context=context)

def page(request, num, year):
    context = {
        "title":"Awesome",
        "page":num
        }
    return render(request, "index.html",context=context)

def RestClimb(request):
    if request.method == 'GET':
        climbs = models.ClimbModel.objects.all()
        list_of_climbs = []
        for item in climbs:
            list_of_climbs += [{
                "climb":item.climb,
                "id":item.id
            }]
        return JsonResponse(list_of_suggestions,safe=False)
    return HttpResponse("Invalid HTTP Method")
