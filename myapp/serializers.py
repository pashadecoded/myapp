from rest_framework import serializers
from .models import Customer, Meat, Purchase

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class MeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meat
        fields = '__all__'

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'