from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .forms import *
from .models import *

# Create your views here.
def index(request):
    form = TodoForm()
    mydict = {
        'form': form,
        'all_todo_items': Todo.objects.all()
    }
    return render(request, 'todo/index.html', context=mydict)


def submit(request):
    obj = Todo()
    form = TodoForm()
    obj.title = request.POST['title']
    obj.discription = request.POST['discription']
    obj.priority = request.POST['priority']
    obj.save()
    mydict = {
        'form' : form,
        'todo_items': Todo.objects.all()
    }
    return render(request, 'todo/tasks.html', context=mydict)


def delete(request , i):
    item = Todo.objects.get(id=i)
    item.delete()
    mydict = {
        'todo_items': Todo.objects.all()
    }
    # return redirect('todo/tasks.html')
    return render(request, 'todo/tasks.html', context=mydict)

def todolist(request):
    mydict = {
        'todo_items': Todo.objects.all()
    }
    return render(request, 'todo/tasks.html', context=mydict)

def main(request):
    form = TodoForm()
    mydict = {
        'form': form,
        'all_todo_items': Todo.objects.all()
    }
    return render(request, 'todo/index.html', context=mydict)

def sortdata(request):
    mydict = {
        'todo_items': Todo.objects.all().order_by('priority')
    }
    return render(request, 'todo/tasks.html', context=mydict)

def searchtodo(request):
    q = request.POST['query']
    mydict = {
        'todo_items' : Todo.objects.filter(title__contains = q)
    }
    return render(request, 'todo/tasks.html', context=mydict)

def edit(request, i):
    obj = Todo.objects.get(id=i)
    form = TodoForm()
    mydict = {
        'title' : obj.title,
        'discription' : obj.discription,
        'priority' : obj.priority,
        'id' : obj.id,
        'form' : form
    }
    return render(request, 'todo/edit.html', context=mydict)

def update(request, i):
    obj = Todo(id=i)
    obj.title = request.POST['title']
    obj.discription = request.POST['discription']
    obj.priority = request.POST['priority']
    import datetime
    updated_at = datetime.datetime.now()
    obj.created_at = updated_at
    obj.save()
    mydict = {

        'todo_items': Todo.objects.all()
    }
    return render(request, 'todo/tasks.html', context=mydict)