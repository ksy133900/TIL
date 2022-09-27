from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "practies/index.html")


def ping(request):
    return render(request, "practies/ping.html")


def pong(request):
    # print(request)
    # print(request.GET.get('ball'))

    ball = request.GET.get("ball")
    context = {
        "name": ball,
    }

    return render(request, "practies/pong.html", context)
