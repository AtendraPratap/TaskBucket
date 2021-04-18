from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

from .models import *
from .forms import *

def index(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks':tasks, 'form':form}
    return render(request,'myapp/list.html',context)

def updatetask(request,pk):
    tasks = Task.objects.get(id=pk)

    form = TaskForm(instance=tasks)

    if request.method == 'POST':
        form = TaskForm(request.POST,instance=tasks)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}

    return render(request,'myapp/update_task.html',context)

def deletetask(request,pk):
    item = Task.objects.get(id=pk)

    if request.method == "POST":
        item.delete()
        return redirect('/')

    context = {'item':item}
    return render(request,'myapp/delete.html',context)
