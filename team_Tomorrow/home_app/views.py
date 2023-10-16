from django.shortcuts import render

def landing_page(request):
    return render(request,'home/landing_page.html')

def registration_page(request):
    return render(request,'home/registration.html')

# Create your views here.
