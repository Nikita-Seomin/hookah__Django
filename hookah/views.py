from django.http import HttpResponse
from django.shortcuts import render
from .models import *


# Create your views here.


def index(request):
    schedule = Schedule.objects.all()
    context = {
        'schedule': schedule,
    }
    print(schedule)
    return render(request, 'hookah/main.html', context=context)


def advantages(request):
    return HttpResponse(f'Преимущества')


def galary(request):
    return HttpResponse(f'Галерея')


def position(request):
    return HttpResponse(f'Местоположение')
