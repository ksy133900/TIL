from django.shortcuts import render
from .models import Article

guestbook = []

# Create your views here.
def index(request):
    guestbook = Article.objects.all()

    return render(request, "articles/index.html", {"guestbook": guestbook})


def create(request):
    content = request.GET.get("content")
    Article.objects.create(content=content)
    context = {
        "content": content,
    }

    return render(request, "articles/create.html", context)
