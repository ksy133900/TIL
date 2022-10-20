from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
import os


def index(request):
    articles = Article.objects.order_by("-pk")

    context = {
        "articles": articles,
    }
    return render(request, "articles/index.html", context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()

    context = {
        "article": article,
        "comments": article.comment_set.all(),
        "comment_form": comment_form,
    }
    return render(request, "articles/detail.html", context)


@login_required
def create(request):
    if request.method == "POST":
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.user = request.user
            article.save()
            messages.success(request, "글 작성이 완료되었습니다.")
            return redirect("articles:index")
    else:
        article_form = ArticleForm()
    context = {
        "article_form": article_form,
    }
    return render(request, "articles/create.html", context=context)


@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == "POST":
            article_form = ArticleForm(request.POST, request.FILES, instance=article)
            if article_form.is_valid():
                article_form.save()
                messages.success(request, "글 수정 완료")
                return redirect("articles:detail", article.pk)
        else:
            article_form = ArticleForm(instance=article)
        context = {
            "article_form": article_form,
        }
        return render(request, "articles/create.html", context)
    else:

        messages.warning(request, "작성자만 수정할 수 있습니다.")
        return redirect("articles:detail", article.pk)


@login_required
def delete(request, pk):
    temp = Article.objects.get(pk=pk)
    if temp.image:
        os.remove(temp.image.path)
    if temp.images:
        os.remove(temp.images.path)
    Article.objects.get(pk=pk).delete()
    return redirect("articles:index")


@login_required
def comment_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
    return redirect("articles:detail", article.pk)


@login_required
def comment_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect("articles:detail", article_pk)


# Create your views here.
