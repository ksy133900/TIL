import os
from django.shortcuts import render, redirect
from .forms import ArticleForm, CommentForm
from .models import Article, Comment

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
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comment = article.comment_set.all()
    context = {
        "article": article,
        "comment_form": comment_form,
        "comments": comment,
    }
    return render(request, "articles/detail.html", context)


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


def comment_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment_form.save()
    return redirect("articles:detail", article.pk)


def comment_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect("articles:detail", article_pk)
