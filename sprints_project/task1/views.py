from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def Welcome(request):
 # return HttpResponse("Welcome to our site")
  template = loader.get_template('mycv.html')
  return HttpResponse(template.render())

