from django.shortcuts import render


def dollar_graphic(request):
    return render(request, 'dollar_graphic.html')


def euro_graphic(request):
    return render(request, 'euro_graphic.html')
