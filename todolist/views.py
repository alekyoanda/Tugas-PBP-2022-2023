from datetime import datetime
from django.shortcuts import render, redirect
from todolist.models import Task
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.
@login_required(login_url='/todolist/login')
def show_todolist(request):
    user = request.user
    tasks = Task.objects.filter(user=user)
    context = {
        "nama": user.username,
        "tasks": tasks
    }
    return render(request, "todolist.html", context)

def create_task(request):
    if (request.method == "POST"):
        title = request.POST["title"]
        date = datetime.now()
        description = request.POST["description"]
        
        new_task = Task.objects.create(user=request.user, date=date, title=title, description=description)
        return redirect('todolist:show_todolist')

    return render(request, "create_task.html")

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    if request.user.is_authenticated:
        return redirect(reverse('todolist:show_todolist')) 
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login') # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    if request.user.is_authenticated:
        return redirect(reverse('todolist:show_todolist')) 
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def delete_task(request, task_id):
    task_to_delete = Task.objects.get(pk=task_id)
    task_to_delete.delete()
    return redirect('todolist:show_todolist')
    
def selesaikan_task(request, task_id):
    task_to_update = Task.objects.get(pk=task_id)
    task_to_update.is_finished = True
    task_to_update.save()
    return redirect('todolist:show_todolist')