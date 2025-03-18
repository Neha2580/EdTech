# from django.shortcuts import render
from django.template import loader 
from django.http import HttpResponse
from .models import events

def event1(request):
    template = loader.get_template('home_page.html')
    return HttpResponse(template.render())

def eventdata(request):
    edata = events.objects.all().values()
    template = loader.get_template('eventdata.html')
    context = {
        'edata' : edata,
    }
    return HttpResponse(template.render(context, request))

# Create your views here.
