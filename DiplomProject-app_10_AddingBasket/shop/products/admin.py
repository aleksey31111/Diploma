from django.contrib import admin
from .models import ProductCategory, Product, Basket
    # ProfitablePropositionCategory, ProfitableProposition,


class ProductAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'category': ('name',)}
    list_display = ('id', 'name', 'quantity', 'price',
                    'category', 'short_description',
                    'image',
                    'time', 'time_update',
                    )
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description', 'short_description')
    list_editable = ('short_description',)
    list_filter = ('time',)
    ordering = ("-time",)


class ProductCategoryAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'category': ('name',)}
    list_display = ('id', 'name', 'description', 'time')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')
    list_editable = ('description',)
    list_filter = ('time',)


# class ProfitablePropositionAdmin(admin.ModelAdmin):
#     # prepopulated_fields = {'category': ('name',)}
#     list_display = ('id', 'name', 'quantity', 'new_price', 'old_price',
#                     'category', 'short_description',
#                     'image',
#                     'time', 'time_update',
#                     )
#     list_display_links = ('id', 'name')
#     search_fields = ('name', 'description', 'short_description')
#     list_editable = ('short_description',)
#     list_filter = ('time',)
#     ordering = ("-time",)


# class ProfitablePropositionCategoryAdmin(admin.ModelAdmin):
#     # prepopulated_fields = {'category': ('name',)}
#     list_display = ('id', 'name', 'description', 'time')
#     list_display_links = ('id', 'name')
#     search_fields = ('name', 'description')
#     list_editable = ('description',)
#     list_filter = ('time',)


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
# admin.site.register(ProfitableProposition, ProfitablePropositionAdmin)
# admin.site.register(ProfitablePropositionCategory, ProfitablePropositionCategoryAdmin)
admin.site.register(Basket)