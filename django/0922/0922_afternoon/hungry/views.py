from django.shortcuts import render
import random
# Create your views here.hj

def dinner(request):
    foods = ['삼겹살', '돈까스', '카레', '햄버거']
    food_img = ['https://pds.joongang.co.kr/news/component/htmlphoto_mmdata/201702/27/117f5b49-1d09-4550-8ab7-87c0d82614de.jpg',
                'https://w.namu.la/s/05876ba153ccefcc901768e02f6d6da1e40920e5f9264e11e72f1c0ba7af0ae23ea0f7d2676ee5680d1ac133716d091a45d07919e9f523d1d619732f7b83974262ef9d4e73a2220e77166dfa460434571062091f448f259599aabe2ed23cb57fd68b58e0b6eb5d30c4a9ee88d856c685',
                 'https://recipe1.ezmember.co.kr/cache/recipe/2020/10/13/4bef6dd54a1395e9920a3489839317b51.jpg',
               'https://newsimg.hankookilbo.com/cms/articlerelease/2021/04/29/62a1cda6-ec70-44a8-811c-fbc6300a18ed.png',]
    food = random.choice(foods)
    img = food_img[foods.index(food)]

    context ={
        'menu': food,
        'images':img,
    }
    
    return render(request, 'dinner.html', context)

def lotto(request):
    number = random.sample(range(1,46),6)
    number2 = random.sample(range(1,46),6)
    number3 = random.sample(range(1,46),6)
    number4 = random.sample(range(1,46),6)
    number5 = random.sample(range(1,46),6)
    
    context = {
        'number': number,
        'number2':number2,
        'number3':number3,
        'number4':number4,
        'number5':number5,
    }
    
    return render(request, 'lotto.html', context)
