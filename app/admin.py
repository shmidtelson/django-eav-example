from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from .models import *


class ProductTypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(ProductType, ProductTypeAdmin)


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)


class ProductAttributeValueInline(admin.TabularInline):
    model = ProductAttributeValue
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductAttributeValueInline
    ]


admin.site.register(Product, ProductAdmin)


class AttributeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Attribute, AttributeAdmin)


class ProductAttributeValueAdmin(admin.ModelAdmin):
    pass


admin.site.register(ProductAttributeValue, ProductAttributeValueAdmin)
