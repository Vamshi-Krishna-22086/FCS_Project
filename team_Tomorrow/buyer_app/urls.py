from django.urls import path
from . import views

urlpatterns = [
    path('', views.buyer_login, name='buyer_login'),
    path('buyer-home/', views.buyer_home, name='buyer_home'),
    path('buyer-query/', views.Querylist, name='buyer_query'),
]