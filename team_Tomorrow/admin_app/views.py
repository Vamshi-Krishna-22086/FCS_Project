from django.shortcuts import render, redirect
from home_app.models import Seller
from home_app.models import Seller, Buyer
from django.http import JsonResponse
import requests
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# admin_kyc before login
# @login_required(login_url='my_admin/')
def admin_kyc(request):
    if request.method == 'POST':
        # Get data from the request
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Create a JSON object
        user_data = {
            'email': username,
            'password': password
        }

        # Send the JSON object to an API
        api_url = 'https://192.168.3.39:5000/kyc'  # Replace with your API endpoint
        response = requests.post(api_url, json=user_data, verify=False)

        # Check if the request was successful
        if response.status_code == 200:
            # Get the JSON response from the API
            api_response = response.json()
            # print(api_response)
            # return JsonResponse(api_response)

            if api_response.get('status') == "success" and username == "vamshi22086@iiitd.ac.in": 
                return redirect('admin-home/')
            else :
                # Display an error message on the login page
                messages.error(request, 'Enter correct credentials')
        else:
            # Handle the error if the API request fails
            messages.error(request, f'API request failed with status code: {response.status_code}')


    return render(request, 'admin_kyc.html')

def admin_login(request):
    return render(request,'admin_login.html')

def admin_home(request):
    return render(request,'admin_home.html')

# deleting a user
def admin_delete_seller(request):
    d_id = request.POST['d_id']
    d_email = request.POST['d_email']
    d_id = int(d_id)
    d_user = Seller.objects.get(id=d_id)
    d_user.delete()
    context = create_seller_data()
    return render(request, 'admin_seller.html', context)

def create_seller_data():
    seller_data = Seller.objects.all()
    userlist = []
    for seller in seller_data:
        users = {}
        users['id'] = seller.id
        users['email'] = seller.email
        users['name'] = seller.name
        users['mobile'] = seller.mobile
        users['city'] = seller.city
        users['state'] = seller.state
        users['country'] = seller.country
        users['file'] = seller.file
        userlist.append(users)

    context = {
        'title': 'Seller Details',
        'userlist': userlist
    }
    return context.copy()

def admin_seller(request):
    context = create_seller_data()
    return render(request, 'admin_seller.html', context)

# Create your views here.
# functions for buyer

def create_buyer_data():
    buyer_data = Buyer.objects.all()
    userlist = []
    for buyer in buyer_data:
        users = {}
        users['id'] = buyer.id
        users['email'] = buyer.email
        users['name'] = buyer.name
        users['mobile'] = buyer.mobile
        users['city'] = buyer.city
        users['state'] = buyer.state
        users['country'] = buyer.country
        users['file'] = buyer.file
        userlist.append(users)

    context = {
        'title': 'Buyer Details',
        'userlist': userlist
    }
    return context.copy()

def admin_buyer(request):
    context = create_buyer_data()
    return render(request, 'admin_buyer.html', context)


def admin_delete_buyer(request):
    d_id = request.POST['d_id']
    d_email = request.POST['d_email']
    d_id = int(d_id)
    d_user = Buyer.objects.get(id=d_id)
    d_user.delete()
    context = create_buyer_data()
    return render(request, 'admin_buyer.html', context)

