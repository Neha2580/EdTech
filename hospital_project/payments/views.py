# from django.shortcuts import render

from django.template import loader 
from django.http import HttpResponse
from .models import payementsnew
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

def payment(request):
    template = loader.get_template('paymentshome.html')
    return HttpResponse(template.render())

def paymentsdata(request):
    pdata = payementsnew.objects.all().values()
    template = loader.get_template('paymentsdata.html')
    context ={
        'pdata':pdata,
    }
    return HttpResponse(template.render(context,request))

def paymentsdata(request):
    template = loader.get_template('paymentsdatawrite.html')
    return HttpResponse(template.render())

@csrf_exempt
def paymentsdatawrite(request):
    if request.method == 'POST':
        Name = request.POST.get('Name')
        Remarks = request.POST.get('Remarks')
        consultationFee = request.POST.get('consultationFee')

        temp = payementsnew(
            Name = Name,
            Remarks = Remarks,
            consultationFee = consultationFee,
        )
        temp.save()
        return redirect("/")
    else:
        return HttpResponse("Invalid request method...")




# Create your views here.
