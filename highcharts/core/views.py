from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def dollar_graphic(request):
    return render(request, 'dollar_graphic.html')


def euro_graphic(request):
    return render(request, 'euro_graphic.html')


def product_graphic(request):
    return render(request, 'product_graphic.html')
