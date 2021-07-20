from rest_framework import viewsets, permissions
from rest_framework.decorators import action

from app.models import Product, ProductType, ProductAttributeValue, Attribute
from app.serializers import ProductSerializer, ProductTypeSerializer, ProductAttributeValueSerializer, \
    AttributeSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]


class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    permission_classes = [permissions.AllowAny]


class ProductAttributeValueViewSet(viewsets.ModelViewSet):
    queryset = ProductAttributeValue.objects.all()
    serializer_class = ProductAttributeValueSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        product_id = request.GET.get('product_id', None)
        if product_id:
            self.queryset = ProductAttributeValue.objects.filter(product_id=product_id)
        return super(ProductAttributeValueViewSet, self).list(request, *args, **kwargs)

    @action(detail=False, methods=['get'])
    def search_attribute_values(self, request):
        product_type_id = request.GET.get('product_type_id', None)
        attribute_id = request.GET.get('attribute_id', None)

        if product_type_id and attribute_id:
            self.queryset = ProductAttributeValue.objects.filter(
                product__product_type_id=product_type_id,
                attribute_id=attribute_id
            )

        return super(ProductAttributeValueViewSet, self).list(request)


class AttributeViewSet(viewsets.ModelViewSet):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['get'])
    def search_not_defined_attributes(self, request):
        product_type_id = request.GET.get('product_type_id', None)

        if product_type_id:
            self.queryset = Attribute.objects.filter(
                product_types=product_type_id,
            )

        return super(AttributeViewSet, self).list(request)
