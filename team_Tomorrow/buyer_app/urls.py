from django.urls import path
from . import views

urlpatterns = [
    path('', views.buyer_login, name='buyer_login'),
    path('buyer-home/', views.buyer_home, name='buyer_home'),
    path('buyer-home1/', views.buyer_home1, name='buyer_home1'),
    path('buyer-query/', views.Querylist, name='buyer_query'),
    path('buyer-home/property-detail/', views.property_detail, name="property-detail"),
    path('buyer-home/pay-success/', views.success, name="pay-success"),
    path('buyer-home/digital-contract/', views.digital_contract, name="digital-contract"),
    path('buyer-home/buyer-profile' , views.view_profile , name='buyer_profile'),
    
]