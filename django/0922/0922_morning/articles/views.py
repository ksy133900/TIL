from multiprocessing import context
import random
from django.shortcuts import render

# Create your views here.
def index(request):
    
    names = ['josie', 'john', 'jonadan', 'sharon']
    name = random.choice(names)
    
    context = {
        'name': name,
        'greeting': [
            '안녕하세요','hi', 'hello', 'ni-hao',      
        ],
    }
    
    return render(request, 'index.html', context)

def welcome(request, name):
    
    context = {
        'name': name,
        'greetings': [
            '안녕하세요','hi', 'hello', 'ni-hao',      
        ],
    }
    
    return render(request, 'welcome.html', context)