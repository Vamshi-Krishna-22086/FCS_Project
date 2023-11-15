from django.shortcuts import render
from home_app.models import Buyer, Listings
from django.contrib.auth.hashers import make_password,check_password
from django.db.models import  FloatField
from django.db.models.functions import Cast
import razorpay
from .models import Property
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def buyer_login(request):
    return render(request,'buyer_home/buyer_login.html')

def property_detail(request):
    if request.method == "POST" or request.method == "GET":
        title = request.GET.get("title")
        amount = request.GET.get("price")
        property_id = request.POST.get("property_id")
        
        # amount = int(request.POST.get("price")) * 100
        client = razorpay.Client(auth =("rzp_test_1r5QwzfBXGKTTZ", "8avjvrHMfFkiyua1E0dnM4vM"))
        payment = client.order.create({'amount':amount, 'currency':'INR', 'payment_capture':'1'})
        mydata = {}
        mydata['title']=title
        mydata['amount']=amount
        mydata['payment']=payment
        print(title)
        print(amount)
        print(payment)
        print("abjh")
        property = Property(name = title , amount = amount, payment_id = payment['id'])
        property.save()
        return render(request , "buyer_home/property_detail.html" , mydata.copy())    
    return render(request,'buyer_home/buyer_home.html')

@csrf_exempt
def success(request):
    if request.method == "POST":
        a = request.POST
        order_id = ""
        for key, val in a.items():
            if key == 'razorpay_order_id':
                order_id = val
                break
        user = Property.objects.filter(payment_id=order_id).first()
        user.paid = True
        user.save()
        
    return render(request,'buyer_home/success.html')

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
        context['buyer_email']=email
        userData=Buyer.objects.all()
        for it in userData:
            print(check_password(password,it.secret))
            if(it.email==email and check_password(password,it.secret)):
                return render(request, 'buyer_home/buyer_home.html', context)

        return render(request, 'buyer_home/buyer_login.html')
    return render(request, 'buyer_home/buyer_login.html')

def buyer_home1(request):

    if(request.method=="POST" or request.method=="GET"):
        
        email=request.POST['username']
        seller_email = email
        context = create_listings()
        context['buyer_email']=email
        return render(request, 'buyer_home/buyer_home.html', context)

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
            

def digital_contract(request):
    return render(request, 'buyer_home/digital_contract.html')

def view_profile(request):
    data={}
    if(request.method=="POST"):
        email=request.POST['extra_mail_1']
        print(email)
        seller_data=Buyer.objects.get(email=email)
        data['email']=email
        data['name']=seller_data.name
        data['city']=seller_data.city
        data['state']=seller_data.state
        data['country']=seller_data.country
        data['mobile']=seller_data.mobile
        data['gender']=seller_data.gender
        return render(request, 'buyer_home/buyer_profile.html',data)
    else:
        return render(request, 'buyer_home/buyer_login.html')



