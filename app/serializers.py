from rest_framework import serializers

from app.models import Product, ProductType, ProductAttribute, Attribute, AttributeValue


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


class AttributeValueSerializer(serializers.ModelSerializer):
    attribute = AttributeSerializer(read_only=True, many=False)

    class Meta:
        model = AttributeValue
        fields = ['id', 'value', 'attribute']


class ProductAttributeSerializer(serializers.ModelSerializer):
    attribute_value = AttributeValueSerializer(read_only=True, many=False)
    attribute_value_id = serializers.PrimaryKeyRelatedField(
        queryset=AttributeValue.objects.all(), source='attribute_value', write_only=True)

    ## Нужны валидаторы при создании, чтобы мы не могли 2 раза в один и тот же продукт создать
    class Meta:
        model = ProductAttribute
        fields = ['id', 'product', 'attribute_value_id', 'attribute_value']
