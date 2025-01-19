from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Basic route for the home page
    path('browse', views.browse, name='browse'),  # Basic route for the home page
]