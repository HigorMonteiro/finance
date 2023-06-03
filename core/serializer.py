from rest_framework import serializers
from .models import Bill, BillCard, CreditCard, Category


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bill
        fields = '__all__'


class BillCardSerializer(serializers.ModelSerializer):
    class Meta:

      model=BillCard
      fields = '__all__'


class CreditCardSerializer(serializers.ModelSerializer):
    class Meta:
      model=CreditCard
      fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
      model=Category
      fields = '__all__'