from django.shortcuts import render
from home_app.models import Seller

def seller_login(request):
    return render(request,'seller_home/seller_login.html')


def seller_home(request):
    if(request.method=="POST"):
        print("Successful")
        email=request.POST['username']
        seller_email = email
        password=request.POST['password']
        userData=Seller.objects.all()
        for it in userData:
            if(it.email==email and it.secret==password):
                # context = create_listings(email)
                return render(request, 'seller_home/seller_home.html')
        # print(userData)
    return render(request, 'seller_home/seller_login.html')

# Create your views here.
