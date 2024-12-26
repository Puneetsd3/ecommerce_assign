from rest_framework import serializers

class CartSerializer(serializers.Serializer):
    item = serializers.CharField(max_length=100)
    price = serializers.FloatField()

class OrderSerializer(serializers.Serializer):
    user_id = serializers.CharField(max_length=100)
    total_amount = serializers.FloatField()
    items = serializers.ListField(child=serializers.DictField())

class DiscountCodeSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=20)
