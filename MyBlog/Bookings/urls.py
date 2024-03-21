from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def mi_vista(xx):
    return HttpResponse("Esta es otra rama")

urlpatterns = [
    path("", mi_vista)
]