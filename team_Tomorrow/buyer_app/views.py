from django.shortcuts import render
from home_app.models import Buyer, Listings
from django.contrib.auth.hashers import make_password,check_password
from django.db.models import  FloatField
from django.db.models.functions import Cast
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
    context = create_listings()
    if(request.method=="POST"):
        
        email=request.POST['username']
        seller_email = email
        password=request.POST['password']
        context = create_listings()
        userData=Buyer.objects.all()
        for it in userData:
            print(check_password(password,it.secret))
            if(it.email==email and check_password(password,it.secret)):
                return render(request, 'buyer_home/buyer_home.html', context)

        return render(request, 'buyer_home/buyer_login.html')
    return render(request, 'buyer_home/buyer_login.html')


def Querylist(request):
    if (request.method=="POST"):
        location = request.POST['location']
        budget = request.POST['budget']

        print("location === " , location)
        print("budget === " , budget)

        if location == 'all':
            context = create_listings()
            if (budget):
                budget = int(budget)
                context = Listings.objects.annotate(
                    price_as_float=Cast('price', FloatField())
                    ).filter(price_as_float__lt=budget)
                print(context)
                context = {'title' : 'listings','listings' : context}
            return render(request, 'buyer_home/buyer_home.html' , context)

        if location and budget:
                budget = float(budget)
                listings = Listings.objects.annotate(
                    price_as_float=Cast('price', FloatField())
                    ).filter(location=location, price_as_float__lt=budget)
                return render(request, 'buyer_home/buyer_home.html', {'title' : 'listings',
        'listings' : listings})
            
            
        
        elif location:
                listings = Listings.objects.filter(location=location)
                return render(request, 'buyer_home/buyer_home.html', {'title' : 'listings',
        'listings' : listings})
        
        elif  budget:
                budget = float(budget)
                listings = Listings.objects.annotate(
                    price_as_float=Cast('price', FloatField())
                    ).filter(price_as_float__lt=budget)
                print(context)
                return render(request, 'buyer_home/buyer_home.html', {'title' : 'listings',
        'listings' : listings})
            





