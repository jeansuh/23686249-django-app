from django.shortcuts import render
from django.http import HttpResponse

def index(reqeust):
    return HttpResponse("Hello, world.You're at the polls index.")
# Create your views here.
