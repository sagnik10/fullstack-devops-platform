from django.shortcuts import render
from .services import create_order

def checkout(request):
    order=create_order(999)
    return render(request,"payments/checkout.html",{"order":order})
