from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse


# Create your views here.
class HelloWorld(View):
    def get(self, request):
        return HttpResponse("<h1>Hello world!</h1>")
