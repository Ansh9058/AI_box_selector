
from rest_framework import serializers
class OrderItemSerializer(serializers.Serializer):
    product_id=serializers.IntegerField()
    quantity=serializers.IntegerField(min_value=1)
class OrderInputSerializer(serializers.Serializer):
    items=OrderItemSerializer(many=True)
