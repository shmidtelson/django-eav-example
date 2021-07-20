from django.db import models
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField


class ProductType(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=255, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name


class Category(MPTTModel):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=120, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    product_type = models.ForeignKey(
        ProductType, related_name="products", on_delete=models.CASCADE, null=True, blank=True
    )
    title = models.CharField(max_length=200, null=False)
    slug = models.SlugField(max_length=120, unique=True)
    category = TreeManyToManyField(Category, blank=True)

    def __str__(self):
        return self.title


class Attribute(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250, unique=True, allow_unicode=True)
    product_types = models.ManyToManyField(
        ProductType,
        blank=True,
        related_name="product_attributes"
    )

    def __str__(self):
        return self.name


class ProductAttributeValue(models.Model):
    product = models.ForeignKey(
        Product, related_name="product", on_delete=models.CASCADE, null=True
    )
    attribute = models.ForeignKey(Attribute, related_name="product_attribute_value", on_delete=models.RESTRICT,
                                  null=True)
    value = models.CharField(max_length=255)

    class Meta:
        unique_together = ("product", "attribute", "value")

    def __str__(self):
        return self.value
