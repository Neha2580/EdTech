# from django.shortcuts import render
from django.template import loader 
from django.http import HttpResponse

def careers(request):
    template = loader.get_template('careershome.html')
    return HttpResponse(template.render())

# Create your views here.
