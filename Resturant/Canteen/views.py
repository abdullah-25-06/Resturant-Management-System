from django.shortcuts import render
from django.http import HttpResponse
from .models import MenuOrder
import datetime 
# Create your views here.

def index(request):
    return render(request,'Canteen/index (1).html')

def Order(request,id):
    if request.method == "POST":
        data = request.POST.get('button1').split("+")
        MenuOrder.objects.create(
            item_name=data[1],
            item_price= data[0],
            id= request.user,
            ordertime=datetime.datetime.now().time(),
            orderdate=datetime.datetime.now().date()
        )
        return HttpResponse(data)
    return HttpResponse('Working')