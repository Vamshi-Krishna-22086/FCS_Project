from rest_framework import serializers
from home_app.models import  Listings

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Listings
        fields = '__all__'
