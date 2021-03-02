from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
import random
from tasklist.models import Task

def index(request):
    tasks = Task.objects.all
    return render(request, 'tasklist/index.html', {'tasks': tasks})

def detail(request, task_id):
    task = Task.objects.get(pk=task_id)
    return render(request, 'tasklist/detail.html', {'task':task})

def create(request):
    if request.method == 'POST':
        task = Task.objects.create(
            name = request.POST['name']
        )
        return redirect('detail', task.id)
    return render(request, 'tasklist/create.html')

def update(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        task.name = request.POST['name']
        task.save()
        return redirect('detail', task.id)
    return render(request, 'tasklist/update.html', {'task':task})

def destroy(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('index')
