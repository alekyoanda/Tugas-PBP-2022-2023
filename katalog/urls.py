# TODO: Implement Routings Here
from django.urls import path
from . import views

app_name = 'katalog'

urlpatterns = [
    path('', views.index, name="index")
]