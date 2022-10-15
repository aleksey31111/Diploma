from django.contrib import admin
from .models import ProductCategory, Product, Basket
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class ProductAdminForm(forms.ModelForm):
    name = forms.CharField(widget=CKEditorUploadingWidget())
    description = forms.CharField(widget=CKEditorUploadingWidget())
    short_description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Product
        fields = '__all__'


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('id', 'name', 'quantity', 'price',
                    'cat', 'short_description',
                    'description', 'image',
                    'time', 'time_update',
                    )
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description', 'short_description')
    list_editable = ('short_description', 'description')
    list_filter = ('time',)
    fields = ('name', 'slug', 'quantity', 'price',
              'cat', 'short_description',
              'image',
              'time', 'time_update',)
    readonly_fields = ('image', 'time', 'time_update')
    ordering = ("-time",)


class ProductCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('id', 'name', 'description', 'time')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')
    list_editable = ('description',)
    list_filter = ('time',)


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Basket)

admin.site.site_header = "Админ-Панель Магазина"
admin.site.site_title = "Админ-Панель Магазина"
