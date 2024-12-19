from django.shortcuts import render
from django.views import View

# Create your views here.
def func_example(request):
    return render(request, 'func_template.html')


class class_example(View):
    def get(self, request):
        return render(request, 'class_template.html')
