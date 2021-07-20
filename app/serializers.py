from rest_framework import serializers

from app.models import Product, ProductType, ProductAttributeValue, Attribute


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'slug', 'product_type']


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ['id', 'name', 'slug']


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ['id', 'name', 'slug']


class ProductAttributeValueSerializer(serializers.ModelSerializer):
    attribute = AttributeSerializer(read_only=True, many=False)
    attribute_id = serializers.PrimaryKeyRelatedField(
        queryset=Attribute.objects.all(), source='attribute', write_only=True)

    class Meta:
        model = ProductAttributeValue
        fields = ['id', 'product','attribute_id', 'attribute', 'value']
