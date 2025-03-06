# from django.shortcuts import render

from django.template import loader 
from django.http import HttpResponse

def payments(request):
    template = loader.get_template('paymentshome.html')
    return HttpResponse(template.render())


# Create your views here.
