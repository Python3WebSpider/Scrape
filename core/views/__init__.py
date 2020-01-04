from .movie import *
from .login1 import *
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
