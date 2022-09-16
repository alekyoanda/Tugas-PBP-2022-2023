from django.urls import path
from . import views

app_name = 'mywatchlist'

urlpatterns = [
    path('', views.index, name="index"),
    path('html/', views.show_html, name="show_html"),
    path('json/', views.show_json, name="show_json"),
    path('xml/', views.show_xml, name="show_xml")
]
