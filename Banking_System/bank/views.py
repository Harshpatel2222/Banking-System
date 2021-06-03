from django.shortcuts import render
import requests

# Create your views here.
from .models import *
from django.contrib import messages

def home_view(request):
    context={}
    return render(request,'index.html',context)

def new_customer(request):
    if request.method == "POST":
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        current_balance = request.POST.get('current_balance')
        new_customer = NewCustomer(name=name, number=number, email=email, current_balance=current_balance)
        new_customer.save()
        messages.success(request, 'Your form has been submitted successfully!')

    return render(request, "new_customer.html")
    