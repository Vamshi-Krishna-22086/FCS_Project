from django.shortcuts import render,redirect
from home_app.models import Seller, Listings
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
from django.contrib.auth import logout



def seller_login(request):
    return render(request,'seller_home/seller_login.html')

def seller_logout(request):
    logout(request)
    return redirect('/')

def edit_listing_page(request):
    id1=request.POST['extra_field_id']
    post=Listings.objects.get(id=id1)
    
    my_post = {}
    my_post['id'] = post.id
    my_post['title'] = post.title
    my_post['location'] = post.location
    my_post['price'] = post.price
    my_post['description'] = post.description
    my_post['posted_by'] = post.posted_by
    my_post['seller_contact'] = post.contact
    my_post['img'] = post.img
    my_post['email'] = post.email
    # print(my_post['description'])
    return render(request,'seller_home/edit_listing.html',my_post.copy())

def edit_listing_save(request):
    if(request.method=="POST"):
        id1=request.POST['extra_field_id']
        print("seller__listing_edit_successful")
        building_name=request.POST['building_name']
        location=request.POST['location']
        price=request.POST['price']
        owner_name=request.POST['owner_name']
        mobile=request.POST['mobile']
        description=request.POST['description']
        email=request.POST['email']
        # building_img=request.POST['building_img']
        seller_email=request.POST['email']
        id1=int(id1)
        
        edit_record=Listings.objects.filter(id=id1)
        edit_record.update(title=building_name,location=location,price=price,posted_by=owner_name,contact=mobile,description=description,email=email)
        messages.warning(request, 'seller__listing_edit_successful')
        context = create_listings(seller_email)
        return render(request, 'seller_home/seller_home.html', context)
    else:
        print("seller__listing_save_unsuceesful")

    return render(request,'seller_home/seller_home.html')
    
    

def add_listing(request):
    email=request.POST['extra_field_3']
    # print(email)
    context = {
        'seller_email': email
    }
    return render(request, 'seller_home/add_listing.html',context.copy())

def view_profile(request):
    data={}
    print(request)
    if(request.method=="POST" or request.method=="GET"):
        try:
            email=request.POST['extra_mail_1']
        except:
            return render(request, 'seller_home/seller_login.html')
        seller_data=Seller.objects.get(email=email)
        data['email']=email
        data['name']=seller_data.name
        data['city']=seller_data.city
        data['state']=seller_data.state
        data['country']=seller_data.country
        data['mobile']=seller_data.mobile
        data['gender']=seller_data.gender
        return render(request, 'seller_home/seller_profile.html',data)
    else:
        return render(request, 'seller_home/seller_login.html')

def delete_listing(request):
    id1=request.POST['extra_field_1']
    seller_email=request.POST['extra_field_2']
    id1=int(id1)
    dele=Listings.objects.get(id=id1)
    dele.delete()
    context = create_listings(seller_email)
    print("------>")
    print(seller_email)
    return render(request, 'seller_home/seller_home.html', context)

def create_listings(email):
    myListings = Listings.objects.all()
    listing = []
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
            my_post['email'] = post.email
            listing.append(my_post)

    context = {
        'title' : 'listings',
        'listings' : listing
    }
    return context.copy()

def seller_home1(request):
    if(request.method=="POST"):
        
        email=request.POST['username']
        
        userData=Seller.objects.all()
        for it in userData:
            # print(check_password(password,it.secret))
            if(it.email==email):
                context = create_listings(email)
                context['seller_email']=email
                print(context)
                return render(request, 'seller_home/seller_home.html', context)
        # print(userData)
    return render(request, 'seller_home/seller_login.html')


def seller_home(request):
    if(request.method=="POST"):
        
        email=request.POST['username']
        password=request.POST['password']
        
        userData=Seller.objects.all()
        for it in userData:
            # print(check_password(password,it.secret))
            if(it.email==email and check_password(password,it.secret)):
                context = create_listings(email)
                context['seller_email']=email
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
        return render(request,'seller_home/seller_login.html')
    else:
        print("seller__listing_save_unsuceesful")

    return render(request,'seller_home/add_listing.html')
# Create your views here.
