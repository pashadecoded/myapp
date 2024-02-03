from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Customer, Meat, Purchase
from .serializers import CustomerSerializer, MeatSerializer, PurchaseSerializer


@api_view(['GET', 'POST'])
def customers_list(request):
    if request.method == 'GET':
        # Search functionality based on CustomerID and PhoneNumber
        customer_id = request.query_params.get('customer_id')
        phone_number = request.query_params.get('phone_number')

        if customer_id:
            customers = Customer.objects.filter(CustomerID=customer_id)
        elif phone_number:
            customers = Customer.objects.filter(PhoneNumber=phone_number)
        else:
            customers = Customer.objects.all()

        serializer = CustomerSerializer(customers, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Check for duplicate entry based on FirstName, LastName, and Email
        first_name = request.data.get('FirstName')
        last_name = request.data.get('LastName')
        email = request.data.get('Email')

        existing_customer = Customer.objects.filter(FirstName=first_name, LastName=last_name, Email=email).first()

        if existing_customer:
            return Response({"error": "Duplicate entry already exists."}, status=status.HTTP_400_BAD_REQUEST)

        # If no duplicate, proceed with creating a new entry
        request_data = request.data.copy()
        request_data['CustomerID'] = Customer.objects.count() + 1

        serializer = CustomerSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def customers_detail(request, pk_or_phone):
    try:
        # Check if the provided pk_or_phone is a CustomerID or PhoneNumber
        if pk_or_phone.isdigit():
            customer = Customer.objects.get(CustomerID=pk_or_phone)
        else:
            customer = Customer.objects.get(PhoneNumber=pk_or_phone)

    except Customer.DoesNotExist:
        return Response({"error": "Customer not found."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        # Update customer information
        serializer = CustomerSerializer(customer, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def meats_list(request):
    if request.method == 'GET':
        data = Meat.objects.all()
        serializer = MeatSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MeatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def meats_detail(request, pk):
    try:
        meat = Meat.objects.get(pk=pk)
    except Meat.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = MeatSerializer(meat, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        meat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def purchases_list(request):
    if request.method == 'GET':
        data = Purchase.objects.all()
        serializer = PurchaseSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PurchaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def purchases_detail(request, pk):
    try:
        purchase = Purchase.objects.get(pk=pk)
    except Purchase.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PurchaseSerializer(purchase, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        purchase.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
