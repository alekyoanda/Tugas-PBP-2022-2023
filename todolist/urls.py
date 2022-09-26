import imp
from django.urls import path
from . import views

app_name = "todolist"

urlpatterns = [
    path('', views.show_todolist, name="show_todolist"),
    path('login/', views.login_user, name="login"),
    path('register/', views.register, name="register"),
    path('create-task/', views.create_task, name="create_task"),
    path('logout/', views.logout_user, name="logout")
]
