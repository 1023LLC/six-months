from django.shortcuts import render

from django.http import HttpResponse

from django.views import View

def index(request):
    return HttpResponse('<h1>Hello, 1023Xc!</h1>')

class home(View):
    return HttpResponse('<h1>This is the HomePage</h1>')
