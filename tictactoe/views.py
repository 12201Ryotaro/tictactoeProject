from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def tictactoe(request):
    return HttpResponse("Hello, world.")