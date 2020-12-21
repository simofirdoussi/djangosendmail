from django.urls import path
from . import views 

urlpatterns = [
    path('functioncontact/', views.functioncontact, name='functioncontact'),
    path('classcontact/', views.ContactFormView.as_view(), name='classcontact'),
]