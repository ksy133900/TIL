from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Todo
from datetime import datetime

# Create your views here.


def index(request):
    # complete = request.GET.get("completed") or False
    # completed = Todo.objects.filter(complete=complete)

    todos = Todo.objects.all()

    context = {
        "todos": todos,
        # "completed": completed,
    }

    return render(request, "todo/index.html", context)


def detail(request, pk):
    # get() 메소드를 사용해서 특정 pk의 데이터를 불러온다.
    # 불러온 데이터를 변수에 할당
    todo = Todo.objects.get(id=pk)
    context = {
        "todo": todo,
    }

    return render(request, "todo/detail.html", context)


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


def edit(request, pk):
    todo = Todo.objects.get(id=pk)
    context = {
        "todo": todo,
    }
    return render(request, "todo/edit.html", context)


def update(request, pk):
    todo = Todo.objects.get(id=pk)
    content_ = request.GET.get("content")
    priority_ = request.GET.get("priority")
    deadline_ = request.GET.get("deadline")
    todo.content = content_
    todo.priority = priority_
    todo.deadline = deadline_
    todo.save()
    return redirect("todo:detail", todo.pk)


def complete(request, pk):
    complete = Todo.objects.get(id=pk)
    if complete.completed == False:
        complete.completed = True

        complete.save()
    elif complete.completed == True:
        complete.completed = False
        complete.save()
    return redirect("todo:index")


def complete_list(request):
    dones = Todo.objects.filter(completed=True)
    return render(request, "todo/todo_done_lilst.html", {"dones": dones})
