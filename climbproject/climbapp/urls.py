from django.urls import path
from django.contrib.auth import views as adminviews

from . import views

urlpatterns = [
    path('', views.index),
    path('climbs/', views.rest_climb),
    path("information/", views.information), #add information about climbing page
    path("information/outdoor", views.outdoor), #add information about climbing page
    path("information/indoor", views.indoor), #add information about climbing page
    path("information/equipment", views.equipment),

    #User Authentication
    path('register/', views.register),
    path('login/', adminviews.LoginView.as_view()),
    path('logout/', views.logout_view),
]