from django.urls import path, re_path, include
from django.contrib.auth import views as adminviews

# from .views import live_chat, room

from . import views

app_name = 'climbapp'

urlpatterns = [
    path('', views.index),
    path('climbs/', views.rest_climb),
    path('information/', views.information), #add information about climbing page
    path('information/outdoor', views.outdoor), #add information about climbing page
    path('information/equipment', views.equipment),

    path('comment/<int:climb_id>/', views.comment_view),

    #User Authentication
    path('register/', views.register),
    path('login/', adminviews.LoginView.as_view()),
    path('logout/', views.logout_view),
    path('account/', views.account),

    # Real Time chat
    path('chat/', views.live_chat),
    path('chat/<room_name>/', views.room),
]
