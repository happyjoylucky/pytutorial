from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'uxsample/index.html')


def login(request):
    return render(request, 'uxsample/login.html')


def findpasswd(request):
    return render(request, 'uxsample/forgot-password.html')


def register(request):
    return render(request, 'uxsample/register.html')


def table(request):
    return render(request, 'uxsample/tables.html')


def card(request):
    return render(request, 'uxsample/cards.html')


def chart(request):
    return render(request, 'uxsample/charts.html')


def button(request):
    return render(request, 'uxsample/buttons.html')


def util_ani(request):
    return render(request, 'uxsample/utilities-animation.html')


def util_border(request):
    return render(request, 'uxsample/utilities-border.html')


def util_color(request):
    return render(request, 'uxsample/utilities-color.html')


def util_other(request):
    return render(request, 'uxsample/utilities-other.html')


def err404(request):
    return render(request, 'uxsample/404.html')


def blank(request):
    return render(request, 'uxsample/blank.html')