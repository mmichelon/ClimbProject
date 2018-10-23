from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('', views.RestClimb),
    path('page/<int:year>/<int>:num/', views.page)
]
