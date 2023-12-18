from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Using function based views here


def home(request):
    return render(request, "index.html")
