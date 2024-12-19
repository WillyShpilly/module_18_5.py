"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from tempfile import template

from django.contrib import admin
from django.urls import path

from task5.views import sign_up_by_django, sign_up_by_html
# from task4.views import main_page, shop, shopping_cart
# from task2.views import func_example, class_example

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', func_example),
    # path('index/', class_example.as_view())

    # path('platform/', main_page),
    # path('platform/games/', shop),
    # path('platform/cart/', shopping_cart),
    # path('', index)
    path('', sign_up_by_django),
    path('reg/', sign_up_by_html)
]