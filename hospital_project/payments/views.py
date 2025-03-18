# from django.shortcuts import render

from django.template import loader 
from django.http import HttpResponse
from .models import payments

def payment(request):
    template = loader.get_template('paymentshome.html')
    return HttpResponse(template.render())

def paymentsdata(request):
    pdata = payments.objects.all().values()
    template = loader.get_template('paymentsdata.html')
    context ={
        'pdata':pdata,
    }
    return HttpResponse(template.render(context,request))


# Create your views here.
