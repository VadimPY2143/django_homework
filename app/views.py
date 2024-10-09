from django.shortcuts import render
from django.http import HttpResponse

def show_name_and_surname(request):
    return HttpResponse('Vadym Papusha')


def show_age(request):
    return HttpResponse(16)

def show_hobby(request):
    return HttpResponse('Volleyball')
