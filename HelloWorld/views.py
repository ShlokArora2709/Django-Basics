from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def HelloWorld(request):
    template=loader.get_template('hello.html')
    return HttpResponse(template.render())