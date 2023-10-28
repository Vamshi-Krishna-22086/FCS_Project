from django.shortcuts import render,redirect
from home_app.models import Seller, Listings
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages


def seller_login(request):
    return render(request,'seller_home/seller_login.html')

def add_listing(request):
    return render(request, 'seller_home/add_listing.html')

def view_profile(request):
    return render(request, 'seller_home/seller_profile.html')

def create_listings(email):
    myListings = Listings.objects.all()
    listings = []
    for post in myListings:
        if(post.email == email):
            my_post = {}
            my_post['id'] = post.id
            my_post['title'] = post.title
            my_post['location'] = post.location
            my_post['price'] = post.price
            my_post['description'] = post.description
            my_post['posted_by'] = post.posted_by
            my_post['seller_contact'] = post.contact
            my_post['img'] = post.img
            listings.append(my_post)

    context = {
        'title' : 'listings',
        'listings' : listings
    }
    return context.copy()


def seller_home(request):
    if(request.method=="POST"):
        
        email=request.POST['username']
        password=request.POST['password']
        
        userData=Seller.objects.all()
        for it in userData:
            print(check_password(password,it.secret))
            if(it.email==email and check_password(password,it.secret)):
                context = create_listings(email)
                print(context)
                return render(request, 'seller_home/seller_home.html', context)
        # print(userData)
    return render(request, 'seller_home/seller_login.html')


def add_listing_save(request):
    if(request.method=="POST"):
        print("seller__listing_save_successful")
        building_name=request.POST['building_name']
        location=request.POST['location']
        price=request.POST['price']
        owner_name=request.POST['owner_name']
        mobile=request.POST['mobile']
        description=request.POST['description']
        email=request.POST['email']
        building_img=request.POST['building_img']
        ins=Listings(title=building_name,location=location,price=price,posted_by=owner_name,contact=mobile,description=description,email=email,img=building_img)
        ins.save()
        # else:
        #     messages.warning(request, 'Password and confirm password did not match.')
        return render(request,'seller_home/add_listing.html')
    else:
        print("seller__listing_save_unsuceesful")

    return render(request,'seller_home/add_listing.html')
# Create your views here.
