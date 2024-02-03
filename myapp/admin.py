from django.contrib import admin
from .models import Customer, Meat, Purchase, Archive

admin.site.register(Customer)
admin.site.register(Meat)
admin.site.register(Purchase)
admin.site.register(Archive)
