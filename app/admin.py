from django.contrib import admin
from .models import *


class ProductTypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(ProductType, ProductTypeAdmin)


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)


class AttributeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Attribute, AttributeAdmin)


class AttributeValueAdmin(admin.ModelAdmin):
    pass


admin.site.register(AttributeValue, AttributeValueAdmin)
