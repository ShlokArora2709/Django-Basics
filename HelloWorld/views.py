from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def HelloWorld(request):
    template=loader.get_template('hello.html')
    return HttpResponse(template.render())

def Members(request):
    mymembers=Member.objects.all()
    template=loader.get_template('members.html')
    context={
        'mymembers':mymembers
    }
    return HttpResponse(template.render(context,request))

def details(request,id):
    member=Member.objects.get(id=id)
    template=loader.get_template('details.html')
    context={
        'mymember':member
    }
    return HttpResponse(template.render(context,request))

def main(request):
    return render(request,'main.html')

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))