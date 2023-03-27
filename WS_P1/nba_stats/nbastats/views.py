from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def members(request):
    return render(request, 'startpage.html')


def playersearch(request):
    return render(request, 'player.html')

def seasonsearch(request):
    return render(request, 'seasons.html')
