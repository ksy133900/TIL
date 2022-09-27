from django.shortcuts import render
import random

# Create your views here.


def is_odd_even(request, number):
    if number == 0:
        num_message = f"{number}은 0입니다."
    elif number % 2 == 0:
        num_message = f"{number}(는)은 짝수입니다."
    else:
        num_message = f"{number}(는)은 홀수입니다."
    context = {
        "number": num_message,
    }
    return render(request, "is_odd_even.html", context)


def calculate(request, number1, number2):

    plus = f"{number1} + {number2} = {number1+number2}"
    minus = f"{number1} - {number2} = {number1-number2}"
    gop = f"{number1} X {number2} = {number1*number2}"
    na = f"{number1} // {number2} = {number1//number2}"

    context = {
        "plus": plus,
        "minus": minus,
        "gop": gop,
        "na": na,
    }
    return render(request, "calculate.html", context)


def random_base(request):
    # text = request.GET.get("_text")

    # context = {
    #     "template_text": text,
    # }
    return render(request, "random_base.html")


def random_life(request):
    text = request.GET.get("random")
    animal = ["사자", "토끼", "코끼리", "하마", "소", "강아지", "고양이", "햄스터"]
    animal_rd = random.choice(animal)

    context = {
        "random": text,
        "animal_rd": animal_rd,
    }
    return render(request, "random_life.html", context)


def zlorem(request):
    return render(request, "zlorem.html")


def zlorem_fluits(request):
    cnt_para = int(request.GET.get("para"))
    cnt_words = int(request.GET.get("words"))

    lorems = [[] for _ in range(cnt_para)]
    ran_words = [
        "바나나",
        "짜장면",
        "사과",
        "바나나",
        "딸기",
    ]

    for i in range(len(lorems)):
        while len(lorems[i]) < cnt_words:
            word = random.choice(ran_words)
            lorems[i].append(word)

    context = {"lorems": lorems}
    return render(request, "zlorem_fluits.html", context)
