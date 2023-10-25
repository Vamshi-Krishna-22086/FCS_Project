from django.db import models

class Seller(models.Model):
    email=models.EmailField()
    name=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    secret=models.CharField(max_length=100)
    file=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    
    class Meta:
        db_table="seller_details"

class Buyer(models.Model):
    email=models.EmailField()
    name=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    secret=models.CharField(max_length=100)
    file=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    
    class Meta:
        db_table="buyer_details"

# Create your models here.
