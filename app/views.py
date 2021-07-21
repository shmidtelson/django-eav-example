from rest_framework import viewsets, permissions
from rest_framework.decorators import action

from app.models import Product, ProductType, ProductAttribute, Attribute, AttributeValue
from app.serializers import ProductSerializer, ProductTypeSerializer, ProductAttributeSerializer, \
    AttributeSerializer, AttributeValueSerializer
from djangoProjecteav.settings import CATEGORY_ALL_ID


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]


class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.exclude(product_attributes__product_types=CATEGORY_ALL_ID)
    serializer_class = ProductTypeSerializer
    permission_classes = [permissions.AllowAny]


class ProductAttributeViewSet(viewsets.ModelViewSet):
    queryset = ProductAttribute.objects.all()
    serializer_class = ProductAttributeSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        product_id = request.GET.get('product_id', None)
        if product_id:
            self.queryset = ProductAttribute.objects.filter(product_id=product_id)
        return super(ProductAttributeViewSet, self).list(request, *args, **kwargs)


class AttributeViewSet(viewsets.ModelViewSet):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['get'])
    def search_not_defined_attributes(self, request):
        product_type_id = request.GET.get('product_type_id', None)

        if product_type_id:
            self.queryset = Attribute.objects.filter(
                product_types__in=(product_type_id, CATEGORY_ALL_ID),
            )

        return super(AttributeViewSet, self).list(request)


class AttributeValueViewSet(viewsets.ModelViewSet):
    queryset = AttributeValue.objects.all()
    serializer_class = AttributeValueSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['get'])
    def search(self, request):
        attribute_id = request.GET.get('attribute_id', None)

        if attribute_id:
            self.queryset = AttributeValue.objects.filter(
                attribute_id=attribute_id
            )

        return super(AttributeValueViewSet, self).list(request)
