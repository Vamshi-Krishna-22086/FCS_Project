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


# model for listings
class Listings(models.Model):
    id = models.IntegerField
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    posted_by = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    email = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    
    class Meta:
        db_table="seller_listings"

# Create your models here.
