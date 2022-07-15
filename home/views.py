from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.



def index(request):
    products=Product.objects.all()
    return render(request,'index.html',{'products':products})
    #return HttpResponse("<h1><center>WELCOME TO HOME</center></h1>")
def contact(request):
    return HttpResponse("<h1><center>CONTACT US</center></h1>")
def complaints(request):
    return HttpResponse("<h1><center>COMPLAIN REGISTER</center></h1>")