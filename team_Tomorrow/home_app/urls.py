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
from home_app import views

urlpatterns = [
    path('',views.landing_page,name='landing_page'),
    path('register/',views.registration_page,name='registration_page'),
    path('my_admin/', include('admin_app.urls')),
    path('seller/', include('seller_app.urls')),
    path('lesser/', include('lesser_app.urls')),
    path('register/seller-buyer-registration/', views.seller_buyer_registrations, name='seller-buyer-registration')
]