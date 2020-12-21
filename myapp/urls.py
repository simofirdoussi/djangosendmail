from django.urls import path
from . import views 

urlpatterns = [
    path('functioncontact/', views.functioncontact, name='functioncontact'),
]