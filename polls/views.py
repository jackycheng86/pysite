from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("这是 polls index页面")

def main(request):
    return HttpResponse("这是 polls main页面")
