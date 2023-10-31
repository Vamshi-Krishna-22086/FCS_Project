from django.shortcuts import render,redirect
from home_app.models import Seller,Buyer
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
from twilio.rest import Client
from django.conf import settings
from django.core.mail import send_mail
import random
import requests


def landing_page(request):
    return render(request,'home/landing_page.html')

def generate_random_otp():
    return str(random.randint(1000, 9999))


def registration_page(request):
    my_post = {}
    my_post['mobile'] = request.POST['mobile']
    email=request.POST['mobile']

    otp = generate_random_otp()
    # Make an API request to the temporary email service to send the OTP to the provided email address
    response = requests.post('lerepo6165@hondabbs.com', json={'email': email, 'otp': otp})
    # Handle the response
    # if response.status_code == 200:
    #     return otp
    # else:
    #     return None

    #otp generate end

    return render(request,'home/registration.html',my_post.copy())

def otp_sent(request):
    return render(request,'home/otp.html')

def seller_buyer_registrations(request):
    if(request.method=="POST" and request.POST['user_type']=='seller'):
        print("seller_successful")
        email=request.POST['email']
        name=request.POST['name']
        city=request.POST['city']
        state=request.POST['state']
        country=request.POST['country']
        secret=request.POST['secret']
        confirm_secret=request.POST['confirm_secret']
        mobile=request.POST['mobile']
        file=request.POST['file']
        gender=request.POST['gender']
        if(secret==confirm_secret):
            hash_secret=make_password(secret)
            ins=Seller(email=email,name=name,city=city,state=state,country=country,secret=hash_secret,mobile=mobile,file=file,gender=gender)
            ins.save()
        else:
            messages.warning(request, 'Password and confirm password did not match.')
            return render(request,'home/registration.html')
        
    elif(request.method=="POST" and request.POST['user_type']=='buyer'):
        print("buyer_successful")
        email=request.POST['email']
        name=request.POST['name']
        city=request.POST['city']
        state=request.POST['state']
        country=request.POST['country']
        secret=request.POST['secret']
        confirm_secret=request.POST['confirm_secret']
        mobile=request.POST['mobile']
        file=request.POST['file']
        gender=request.POST['gender']

        if(secret==confirm_secret):
            hash_secret=make_password(secret)
            ins=Buyer(email=email,name=name,city=city,state=state,country=country,secret=hash_secret,mobile=mobile,file=file,gender=gender)
            ins.save()
        else:
            messages.warning(request, 'Password and confirm password did not match.')
            return render(request,'home/registration.html')
    else:
        print("unsuceesful")

    return redirect('/')

# Create your views here.
