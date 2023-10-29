from django.shortcuts import render
from home_app.models import Seller, Listings
from django.contrib.auth.hashers import make_password,check_password
from rest_framework import generics

# Create your views here.

def buyer_login(request):
    return render(request,'buyer_home/buyer_login.html')

def create_listings():
    myListings = Listings.objects.all()
    listings = []
    for post in myListings:
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

def buyer_home(request):

    if(request.method=="POST"):
        
        email=request.POST['username']
        seller_email = email
        password=request.POST['password']
        context = create_listings()
        userData=Seller.objects.all()
        for it in userData:
            print(check_password(password,it.secret))
            if(it.email==email and check_password(password,it.secret)):
                return render(request, 'buyer_home/buyer_home.html', context)

        return render(request, 'buyer_home/buyer_home.html' , context)


def Querylist(request):
    if (request.method=="POST"):
        location = request.POST['location']
        budget = request.POST['budget']

        # print("location === " , location)
        # print("budget === " , type(budget))

        if location == 'all':
            context = create_listings(1) # 1 does not here anything
            if (budget):
                budget = float(budget)
                context = Listings.objects.filter(price__lt=budget)
                print(context)
                context = {'title' : 'listings','listings' : context}
            return render(request, 'buyer_home/buyer_home.html' , context)

        if location and budget:
            try:
                budget = float(budget)
                listings = Listings.objects.filter(location=location, price__lt=budget)
                return render(request, 'buyer_home/buyer_home.html', {'title' : 'listings',
        'listings' : listings})
            
            except ValueError:
                return render(request, 'error_template.html', {'error_message': 'Invalid budget value'})

        
        elif location:
                listings = Listings.objects.filter(location=location)
                return render(request, 'buyer_home/buyer_home.html', {'title' : 'listings',
        'listings' : listings})
        
        elif  budget:
            try:
                budget = float(budget)
                listings = Listings.objects.filter(price__lt=budget)
                return render(request, 'buyer_home/buyer_home.html', {'title' : 'listings',
        'listings' : listings})
            
            except ValueError:
                return render(request, 'error_template.html', {'error_message': 'Invalid budget value'})
           
        

        





