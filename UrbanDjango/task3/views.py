from django.shortcuts import render

# Create your views here.
def main_page(request):
    return render(request, 'main_page.html')


def shop(request):
    title = 'Игрища'
    game1 = 'Atomic Heart'
    game2 = 'Cyberpunk 2077'
    game3 = 'PayDay 2'
    context = {
        'title': title,
        'game1': game1,
        'game2': game2,
        'game3': game3
    }
    return render(request, 'shop.html', context)


def shopping_cart(request):
    return render(request, 'shopping_cart.html')
