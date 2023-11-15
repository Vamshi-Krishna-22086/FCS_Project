from django.shortcuts import render,redirect
from home_app.models import Seller,Buyer
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
#from twilio.rest import Client
from django.conf import settings
from django.core.mail import send_mail
import random
import requests


# user eKYC
def user_ekyc(request):
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

            if api_response.get('status') == "success" : 
                return redirect('register/')
            else :
                # Display an error message on the login page
                messages.error(request, '')
        else:
            # Handle the error if the API request fails
            messages.error(request, f'API request failed with status code: {response.status_code}')


    return render(request, 'user_kyc.html')


def landing_page(request):
    return render(request,'home/landing_page.html')

def generate_random_otp():
    return str(random.randint(1000, 9999))


def registration_page(request):
    my_post = {}
    my_post['mobile'] = request.POST['mobile']
    phone_number=request.POST['mobile']

    otp = generate_random_otp()

    # client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    # message = client.messages.create(
    #     body=f'Your OTP is: {otp}',
    #     from_=settings.TWILIO_PHONE_NUMBER,
    #     to=phone_number
    # )
    #otp generate end

    my_post['generate_otp'] = otp
    print(otp)

    return render(request,'home/registration.html',my_post.copy())

def otp_sent(request):
    return render(request,'home/otp.html')

def seller_buyer_registrations(request):
    user_otp=int(request.POST['user_otp'])
    generate_otp=int(request.POST['generate_otp'])
    if(user_otp!=generate_otp):
        messages.warning(request, 'OTP did not match.')
        return render(request,'home/otp.html')
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
        try:
            email_check=Seller.objects.get(email=email)
            mobile_check=Seller.objects.get(mobile=mobile)
            messages.warning(request, 'mail or mobile is already register')
            return render(request,'home/registration.html')
        except:          
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

        try:
            email_check=Buyer.objects.get(email=email)
            mobile_check=Buyer.objects.get(mobile=mobile)
            messages.warning(request, 'mail or mobile is already register')
            return render(request,'home/registration.html')
        except:          
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
