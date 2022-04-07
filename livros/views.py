from django.shortcuts import render
from .models import Livros 

# Create your views here.

def index(request):
    template_name = "livros/base.html"
    return render(request, template_name)