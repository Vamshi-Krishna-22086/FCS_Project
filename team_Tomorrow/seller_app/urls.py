"""
URL configuration for team_Tomorrow project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from seller_app import views

urlpatterns = [
    path('' , views.seller_login , name='seller-login'),
    path('seller-home/', views.seller_home, name='seller-home'),
    path('add-listing/', views.add_listing, name='add-listing'),
    path('add-listing/add-listing-save/', views.add_listing_save, name='add-listing-save')
]
