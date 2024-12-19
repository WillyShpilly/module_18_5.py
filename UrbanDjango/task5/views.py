from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

# Create your views here.
def sign_up_by_html(request):
    users = ['Dmitry', 'Valeriya', 'Denis', 'Viktoria', 'Barmaley']
    info = {}
    context = {
        'info': info,
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if password == repeat_password and int(age) >= 18 and username not in users:
            return HttpResponse(f"Приветствуем, {username}!")
        if password != repeat_password:
            info.update({'error1': 'Пароли не совпадают'})
        if int(age) < 18:
            info.update({'error2': 'Вы должны быть старше 18'})
        if username in users:
            info.update({'error3': 'Пользователь уже существует'})
    return render(request, 'registration_page.html', context)


def sign_up_by_django(request):
    users = ['Dmitry', 'Valeriya', 'Denis', 'Viktoria', 'Barmaley']
    info = {}
    form = UserRegister()
    context = {
        'info': info,
        'form': form,
    }
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password == repeat_password and int(age) >= 18 and username not in users:
                return HttpResponse(f"Приветствуем, {username}!")
            if password != repeat_password:
                info.update({'error1': 'Пароли не совпадают'})
            if int(age) < 18:
                info.update({'error2': 'Вы должны быть старше 18'})
            if username in users:
                info.update({'error3': 'Пользователь уже существует'})
        else:
            form = UserRegister()
    return render(request, 'registration_page.html', context)


# def index(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']
#             subscribe = form.cleaned_data['subscribe']
#         else:
#             form = ContactForm()
#         return render(request, 'registration_page.html', {'form':form})

# def index(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         subscribe = request.POST.get('subscribe') == 'on'
#
#         print(f"Name: {name}")
#         print(f"Email: {email}")
#         print(f"Message: {message}")
#         print(f"Subscribe: {subscribe}")
#
#         return HttpResponse("Форма успешно отправлена!")
#     return render(request, 'registration_page.html')