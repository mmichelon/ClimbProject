from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('climbs/', views.rest_climb),
    # path("page/"), #add information about climbing page
    path('page/<int:year>/<int>:num/', views.page)
]
