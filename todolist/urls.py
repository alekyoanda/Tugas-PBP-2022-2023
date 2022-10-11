from django.urls import path
from . import views

app_name = "todolist"

urlpatterns = [
    path('', views.show_todolist, name="show_todolist"),
    path('login/', views.login_user, name="login"),
    path('register/', views.register, name="register"),
    path('create-task/', views.create_task, name="create_task"),
    path('logout/', views.logout_user, name="logout"),
    path('delete_task/<int:task_id>', views.delete_task, name="delete_task"),
    path('selesaikan_task/<int:task_id>', views.selesaikan_task, name="selesaikan_task"),
    path('json', views.show_todolist_json, name="json_todolist"),
    path('add', views.add_task_ajax, name="add_task_ajax"),
    path('delete/<int:id>', views.delete_task_ajax, name="delete_task_ajax"),
    path('finish_task/<int:id>', views.finish_task_ajax, name="finish_task_ajax"),
]
