from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

# Create your views here.
users = ['Dmitry', 'Valeriya', 'Denis', 'Viktoria', 'Barmaley']


def sign_up_by_django(request):
    info = {}

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']

            age = form.cleaned_data['age']
            if username in users:
                info['error'] = f"Пользователь {username} уже существует"

            elif len(password) < 8:
                info['error'] = ('Пароль должен быть не менее 8 символов')

            elif repeat_password != password:
                info['error'] = ('Пароли не совпадают')

            elif int(age) < 18:
                info['error'] = ("Вы должны быть старше 18")

            else:
                info['text'] = (f'Приветсвуем, {username}!')

        info['form'] = form

    return render(request, 'registration_page.html', info)


def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if username in users:
            info['error'] = f"Пользователь {username} уже существует"

        elif len(password) < 8:
            info['error'] = ('Пароль должен быть не менее 8 символов')

        elif repeat_password != password:
            info['error'] = ('Пароли не совпадают')

        elif int(age) < 18:
            info['error'] = ("Вы должны быть старше 18")

        else:
            info['text'] = (f'Приветсвуем, {username}!')

    return render(request, 'registration_page.html', info)
