from django.urls import path
from django.contrib.auth import views as adminviews

from . import views

urlpatterns = [
    path('', views.index),
    path('climbs/', views.rest_climb),
    # path("page/"), #add information about climbing page
    path('page/<int:year>/<int>:num/', views.page),
    #User Authentication
    path('register/', views.register),
    path('login/', adminviews.LoginView.as_view()),
]
