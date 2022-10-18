import os
from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article

# Create your views here.


def index(request):
    return render(request, "articles/index.html", {"contents": Article.objects.all()})


def create(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("articles:index")
    context = {
        "form": form,
    }
    return render(request, "articles/create.html", context)


def detail(request, pk):
    return render(
        request, "articles/detail.html", {"content": Article.objects.get(pk=pk)}
    )


def update(request, pk):
    temp = Article.objects.get(pk=pk)
    form = ArticleForm(
        request.POST or None, request.FILES or None, instance=Article.objects.get(pk=pk)
    )
    if form.is_valid():
        if temp.image:
            os.remove(temp.image.path)
        if temp.thumbnail:
            os.remove(temp.thumbnail.path)
        form.save()
        return redirect("articles:detail", pk)
    context = {
        "form": form,
    }
    return render(request, "articles/create.html", context)


def delete(request, pk):
    temp = Article.objects.get(pk=pk)
    if temp.image:
        os.remove(temp.image.path)
    if temp.thumbnail:
        os.remove(temp.thumbnail.path)
    Article.objects.get(pk=pk).delete()
    return redirect("articles:index")
