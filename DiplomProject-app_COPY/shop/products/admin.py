from django.contrib import admin
from .models import ProductCategory, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'quantity', 'price',
                    'category', 'short_description',
                    'image',
                    'time', 'time_update',
                    )
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description', 'short_description')
    list_editable = ('short_description',)
    list_filter = ('time',)


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'time')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')
    list_editable = ('description',)
    list_filter = ('time',)


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
