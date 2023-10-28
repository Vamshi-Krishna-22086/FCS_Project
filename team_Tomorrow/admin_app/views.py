from django.shortcuts import render
from home_app.models import Seller, Buyer


def admin_login(request):
    return render(request,'admin_login.html')

def admin_home(request):
    return render(request,'admin_home.html')

def admin_seller(request):
    context = {}
    context = {
            'title' : 'Seller details',
            'userlist' : [
                {
                    'email' : 'vamshi@gmail.com',
                    'name' : 'VVK Properties',
                    'mobile' : '98274837643',
                    'city' : 'Hyderabad',
                    'state' : 'Telangana',
                    'country' : 'India',
                    'file' : 'vamshi.pdf'
                },
                {
                    'email' : 'vamshi@gmail.com',
                    'name' : 'VVK Properties',
                    'mobile' : '98274837643',
                    'city' : 'Hyderabad',
                    'state' : 'Telangana',
                    'country' : 'India',
                    'file' : 'vamshi.pdf'
                },
                {
                    'email' : 'vamshi@gmail.com',
                    'name' : 'VVK Properties',
                    'mobile' : '98274837643',
                    'city' : 'Hyderabad',
                    'state' : 'Telangana',
                    'country' : 'India',
                    'file' : 'vamshi.pdf'
                }
            ]
        }
    # if(request.method == 'POST'):
        
    return render(request, 'admin_seller.html', context)

# Create your views here.
