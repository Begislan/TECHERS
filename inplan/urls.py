from django.urls import path

from .views import inplan

urlpatterns = [
    path('', inplan)
]
