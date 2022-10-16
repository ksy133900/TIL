from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm


# Create your views here.


def index(request):
    review = Review.objects.order_by("pk")
    context = {
        "review": review,
    }
    return render(request, "review/index.html", context)


def create(request):
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            return redirect("review:index")
    else:
        review_form = ReviewForm()
    context = {
        "review_form": review_form,
    }
    return render(request, "review/new.html", context=context)


def detail(request, pk):
    # 특정 글을 가져온다.
    review = Review.objects.get(pk=pk)
    # template에 객체 전달
    context = {
        "review": review,
    }
    return render(request, "review/detail.html", context)


def update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == "POST":
        # POST : input 값 가져와서, 검증하고, DB에 저장
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            # 유효성 검사 통과하면 저장하고, 상세보기 페이지로
            review_form.save()
            return redirect("review:detail", review.pk)
    else:
        # GET : Form을 제공
        review_form = ReviewForm(instance=review)
    context = {
        "review_form": review_form,
    }
    return render(request, "review/update.html", context)


def delete(request, pk):

    review = Review.objects.get(id=pk)
    review.delete()

    return redirect("review:index")
