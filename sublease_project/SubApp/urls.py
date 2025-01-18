from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Basic route for the home page
]