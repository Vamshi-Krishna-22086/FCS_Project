from django.shortcuts import render
from home_app.models import Seller
from home_app.models import Seller, Buyer


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
