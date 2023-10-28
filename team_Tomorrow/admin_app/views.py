from django.shortcuts import render


def admin_login(request):
    return render(request,'admin_login.html')

def admin_home(request):
    return render(request,'admin_home.html')

# Create your views here.
