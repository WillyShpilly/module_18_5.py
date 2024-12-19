from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.


def shopping_cart(request):
    text = 'Корзина'
    text2 = 'Извините, ваша корзина пуста'
    context = {
        'text': text,
        'text2': text2
    }
    return render(request, 'shopping_cart.html',context)


def shop(request):
    text = 'Игрища'
    list = ['Atomic Heart',
            'Cyberpunk 2077',
            'PayDay 2']
    context = {
        'text': text,
        'games': list
    }
    return render(request, 'shop.html', context)


def main_page(request):
    text = 'Главная страница'
    context = {
        'text': text
    }
    return render(request, 'main_page.html', context)


