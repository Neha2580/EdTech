# from django.shortcuts import render
from django.template import loader 
from django.http import HttpResponse

def doctors(request):
    template = loader.get_template('doctorshome.html')
    return HttpResponse(template.render())

# Create your views here.
