from django.shortcuts import redirect, render

from .forms import CustomUserCreationForm

# from .models import User
from django.contrib.auth import get_user_model

# from django.contrib.auth.forms import UserCreationForm
# from .forms import CustomUserCreationForm

# Create your views here.


def index(request):
    user = get_user_model().objects.order_by("pk")
    context = {
        "user": user,
    }
    return render(request, "accounts/index.html", context)


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:index")
    else:
        form = CustomUserCreationForm()
    context = {"form": form}
    return render(request, "accounts/signup.html", context)


def detail(request, pk):

    user = get_user_model().objects.get(pk=pk)

    context = {
        "user": user,
    }

    return render(request, "accounts/detail.html", context)
