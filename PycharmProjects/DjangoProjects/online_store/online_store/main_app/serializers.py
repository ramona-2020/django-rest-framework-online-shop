from rest_framework import serializers
from rest_framework.fields import DateField, DecimalField
from online_store.main_app.models import Product, Order


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'title', 'price', )


class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'


class MySerializer(serializers.Serializer):

    month = DateField()
    value = DecimalField(
        max_digits=5,
        decimal_places=2
    )

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
