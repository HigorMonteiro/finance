from django.shortcuts import render
from rest_framework import viewsets
from .serializer import BillSerializer, BillCardSerializer, CreditCardSerializer, CategorySerializer
from .models import Bill, BillCard, CreditCard, Category
# Create your views here.


class BillView(viewsets.ModelViewSet):
    serializer_class = BillSerializer
    queryset = Bill.objects.all()


class BillCardView(viewsets.ModelViewSet):
    serializer_class = BillCardSerializer
    queryset = BillCard.objects.all()


class CreditCardView(viewsets.ModelViewSet):
    serializer_class = CreditCardSerializer
    queryset = CreditCard.objects.all()


class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()