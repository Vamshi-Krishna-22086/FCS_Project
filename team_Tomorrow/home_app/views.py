from django.shortcuts import render,redirect
from home_app.models import Seller,Buyer
from django.contrib.auth.hashers import make_password,check_password

def landing_page(request):
    return render(request,'home/landing_page.html')

def registration_page(request):
    return render(request,'home/registration.html')

def seller_buyer_registrations(request):
    if(request.method=="POST" and request.POST['user_type']=='seller'):
        print("seller_successful")
        email=request.POST['email']
        name=request.POST['name']
        city=request.POST['city']
        state=request.POST['state']
        country=request.POST['country']
        secret=request.POST['secret']
        mobile=request.POST['mobile']
        file=request.POST['file']
        gender=request.POST['gender']

        hash_secret=make_password(secret)

        ins=Seller(email=email,name=name,city=city,state=state,country=country,secret=hash_secret,mobile=mobile,file=file,gender=gender)
        ins.save()
    elif(request.method=="POST" and request.POST['user_type']=='buyer'):
        print("seller_successful")
        email=request.POST['email']
        name=request.POST['name']
        city=request.POST['city']
        state=request.POST['state']
        country=request.POST['country']
        secret=request.POST['secret']
        mobile=request.POST['mobile']
        file=request.POST['file']
        gender=request.POST['gender']

        hash_secret=make_password(secret)

        ins=Buyer(email=email,name=name,city=city,state=state,country=country,secret=hash_secret,mobile=mobile,file=file,gender=gender)
        ins.save()
    else:
        print("unsuceesful")

    return redirect('/')

# Create your views here.
