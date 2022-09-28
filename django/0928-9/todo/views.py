from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.


def index(request):
    todos = Todo.objects.all()
    context = {
        "todos": todos,
    }

    return render(request, "todo/index.html", context)


def create(request):
    content = request.GET.get("content")
    priority = request.GET.get("priority")
    deadline = request.GET.get("deadline")

    Todo.objects.create(content=content, priority=priority, deadline=deadline)

    return redirect("todo:index")


def delete(request, pk):

    todo = Todo.objects.get(id=pk)
    todo.delete()

    return redirect("todo:index")


def complete(request, pk):
    complete = Todo.objects.get(id=pk)
    complete.completed = True
    complete.save()

    return redirect("todo:index")
