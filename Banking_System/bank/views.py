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
        new_customer = Customer(name=name, number=number, email=email, current_balance=current_balance)
        new_customer.save()
        messages.success(request, 'Your form has been submitted successfully!')

    return render(request, "new_customer.html")
    
def view_customers(request):
    customers = Customer.objects.all()
    context={'customers' : customers}
    return render(request,'view_customers.html',context)

def customer_details(request, pk):
    customer = Customer.objects.get(id = pk)
    context={'customer':customer}
    return render(request,'customer_details.html',context)