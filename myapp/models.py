# models.py
from django.db import models


class Customer(models.Model):
    CustomerID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    PhoneNumber = models.CharField(max_length=15)
    Email = models.EmailField(max_length=100)
    Address = models.TextField()


class Meat(models.Model):
    MeatID = models.AutoField(primary_key=True)
    MeatType = models.CharField(max_length=50)
    PricePerKg = models.DecimalField(max_digits=10, decimal_places=2)


class Purchase(models.Model):
    PurchaseID = models.AutoField(primary_key=True)
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    MeatID = models.ForeignKey(Meat, on_delete=models.CASCADE)
    PurchaseDate = models.DateField()
    QuantityKg = models.DecimalField(max_digits=10, decimal_places=2)
    TotalPrice = models.DecimalField(max_digits=10, decimal_places=2)


class Archive(models.Model):
    ArchiveID = models.AutoField(primary_key=True)
    OriginalTable = models.CharField(max_length=50)
    OriginalID = models.IntegerField()
    ArchiveDate = models.DateTimeField(auto_now_add=True)
