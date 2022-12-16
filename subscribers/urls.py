from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscribers, name='subscribers'),
]
