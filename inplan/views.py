from django.shortcuts import render
from django.http import HttpResponse

def inplan(request):
    return HttpResponse("<h1>Это страница для инплана</h1>")