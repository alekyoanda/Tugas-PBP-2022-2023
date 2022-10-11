import json
from django.shortcuts import render, redirect
from urllib3 import Retry
from todolist.models import Task
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
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
    if len(tasks) == 0:
        tasks = None
    context = {
        "nama": user.username,
        "tasks": tasks
    }
    return render(request, "todolist_ajax.html", context)

def show_todolist_json(request):
    if request.method == "GET":
        data = Task.objects.filter(user=request.user)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    
def add_task_ajax(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        new_task = Task.objects.create(user=request.user, title=title, description=description)
        
        serialize_json = serializers.serialize('json', [new_task])
        print(serialize_json)
        
        return HttpResponse(serialize_json)

    return JsonResponse({"error": "Not an ajax request"}, status=400)

def delete_task_ajax(request, id):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method == "DELETE":
        task = Task.objects.get(pk=id)
        task.delete()
        return HttpResponse("Success Deleting Task")
    return JsonResponse({"error": "Not an ajax request"}, status=400)

def finish_task_ajax(request, id):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method == "POST":
        task = Task.objects.get(pk=id)
        task.is_finished = True
        task.save()
        return HttpResponse("Success updating task")
    return JsonResponse({"error": "Not an ajax request"}, status=400)

def create_task(request):
    if (request.method == "POST"):
        title = request.POST["title"]
        description = request.POST["description"]
        
        new_task = Task.objects.create(user=request.user, title=title, description=description)
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

