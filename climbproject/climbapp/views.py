from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

#User Authentication
from django.contrib.auth import logout
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Real Time chat
from django.utils.safestring import mark_safe
import json

# Create your views here.
from . import models
from . import forms

@login_required
def index(request):
    comm_form = forms.CommentForm()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form_instance = forms.ClimbForm(request.POST)
        search_instance = forms.searchForm(request.POST)
        if form_instance.is_valid():
            if request.user.is_authenticated:
                climb = models.ClimbModel(
                    climb = form_instance.cleaned_data["climb"],
                    difficulty = form_instance.cleaned_data["difficulty"],
                    outdoor_bool = form_instance.cleaned_data["outdoor_bool"],
                    climb_notes = form_instance.cleaned_data["climb_notes"],
                    author = request.user
                )
                climb.save()
                form_instance = forms.ClimbForm()

    else:
        form_instance = forms.ClimbForm()
        search_instance = forms.searchForm()

    climbs = models.ClimbModel.objects.all()
    context = {
        "title":"Climb to the Max",
        "climbs":climbs,
        "form_instance":form_instance,
        "comm_form":comm_form,
        "search_instance":search_instance
        }
    return render(request, "index.html", context=context)

@login_required
def comment_view(request, climb_id):
    comm_form = forms.CommentForm()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form_instance = forms.CommentForm(request.POST)
        if form_instance.is_valid():
            if request.user.is_authenticated:
                climb_instance = models.ClimbModel.objects.get(pk=climb_id)
                comment = models.CommentModel(
                    comment=form_instance.cleaned_data["comment"],
                    author=request.user,
                    climb=climb_instance
                )
                comment.save()
                # form_instance = forms.CommentForm()
                return redirect("/")
    else:
        form_instance = forms.CommentForm()
    context = {
        "title":"Comment",
        "form_instance":form_instance,
        "climb_id":climb_id
        }
    return render(request, "comment.html", context=context)


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

@login_required
def account(request):
    comm_form = forms.CommentForm()

    # currentUserId = models.User.objects.get(id=request.user.id)
    # userClimbs = models.ClimbModel.objects.filter(author=currentUserId.username)

    # climbs = models.ClimbModel.objects.all()

    userClimbs = models.ClimbModel.objects.filter(author=request.user)

    context = {
        "title": "Account",

        "comm_form":comm_form,

        "climbs":userClimbs,
        }
    return render(request, "registration/account.html", context=context)

def information(request):
    context = {
        "title": "Climbing Information",
        }
    return render(request, "information/information.html", context=context)

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
            # list_of_climbs += [{
            add_to_list = {
                "climb":item.climb,
                "difficulty":item.difficulty,
                "outdoor_bool":item.outdoor_bool,
                "climb_notes":item.climb_notes,
                "author":item.author.username,
                "id":item.id,
                "created_on":item.creation_date,
                "comments":[]
            }
            comment_query = models.CommentModel.objects.filter(climb=item)
            for comm in comment_query:
                add_to_list["comments"] += [{
                    "comment":comm.comment,
                    "id":comm.id,
                    "author":comm.author.username,
                    "created_on":comm.creation_date
                }]
            list_of_climbs += [add_to_list]
        # return JsonResponse(list_of_climbs,safe=False)
        return JsonResponse({"climbs": list_of_climbs})
    else:
        return HttpResponse("Invalid HTTP Method")

def rest_climb_user(request):
    if not request.user.is_authenticated:
        return JsonResponse({"climbs":[]})
    if request.method == 'GET':
        # climbs = models.ClimbModel.objects.all()
        climbs = models.ClimbModel.objects.filter(author=request.user)

        list_of_climbs = []
        for item in climbs:
            # list_of_climbs += [{
            add_to_list = {
                "climb":item.climb,
                "difficulty":item.difficulty,
                "outdoor_bool":item.outdoor_bool,
                "climb_notes":item.climb_notes,
                "author":item.author.username,
                "id":item.id,
                "created_on":item.creation_date,
                "comments":[]
            }
            comment_query = models.CommentModel.objects.filter(climb=item)
            for comm in comment_query:
                add_to_list["comments"] += [{
                    "comment":comm.comment,
                    "id":comm.id,
                    "author":comm.author.username,
                    "created_on":comm.creation_date
                }]
            list_of_climbs += [add_to_list]
        # return JsonResponse(list_of_climbs,safe=False)
        return JsonResponse({"climbs": list_of_climbs})
    else:
        return HttpResponse("Invalid HTTP Method")

def climbSearch(request):
    # if request.method == 'POST':
    #     x = None
    #     form.is_valid()
    #     if forms.has_changed():
    #         x = ClimbModel.objects.all()
    #         if 'climbType' is form.changed_data():
    #             x = x.filter(climbType = form.cleaned_data['climbType'])
    #         return JsonResponse({"climbs": x})
    if not request.user.is_authenticated:
        return JsonResponse({"climbs":[]})
    if request.method == 'POST':
        # climbs = models.ClimbModel.objects.all()
        climbs = models.ClimbModel.objects.filter(climb=form.cleaned_data['climbType'])

        list_of_climbs = []
        for item in climbs:
            # list_of_climbs += [{
            add_to_list = {
                "climb":item.climb,
                "difficulty":item.difficulty,
                "outdoor_bool":item.outdoor_bool,
                "climb_notes":item.climb_notes,
                "author":item.author.username,
                "id":item.id,
                "created_on":item.creation_date,
                "comments":[]
            }
            comment_query = models.CommentModel.objects.filter(climb=item)
            for comm in comment_query:
                add_to_list["comments"] += [{
                    "comment":comm.comment,
                    "id":comm.id,
                    "author":comm.author.username,
                    "created_on":comm.creation_date
                }]
            list_of_climbs += [add_to_list]
        # return JsonResponse(list_of_climbs,safe=False)
        return JsonResponse({"climbs": list_of_climbs})
    else:
        return HttpResponse("Invalid HTTP Method")
# Real Time chat
def live_chat(request):
    return render(request, 'chat/live_chat.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
