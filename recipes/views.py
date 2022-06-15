from multiprocessing import context

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html', context={
        'name': 'Moyses',
    })


def contato(request):
    return HttpResponse("contato")


def sobre(request):
    return HttpResponse("sobre")
