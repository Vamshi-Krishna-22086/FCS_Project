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
from admin_app import views

urlpatterns = [
    # path('' , views.admin_login , name='admin-login'),
    path('' , views.admin_kyc , name='admin-login'),
    path('admin-home/', views.admin_home, name='admin-home'),
    path('admin-home/admin-sellers/', views.admin_seller, name='admin-seller'),
    path('admin-delete-seller/', views.admin_delete_seller, name='admin-delete-seller'),
    path('admin-home/admin-buyers/', views.admin_buyer, name='admin-buyer'),
    path('admin-delete-buyer/', views.admin_delete_buyer, name='admin-delete-buyer')
]
