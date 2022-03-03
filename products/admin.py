from django.contrib import admin

from products.models import Product, ProductCategory

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')  # поля в таблице
    fields = ('name', 'image', 'description', ('price', 'quantity'), 'category')  # поля внутри объекта
    readonly_fields = ('description',)
    search_fields = ('name', 'category__name', )  # category__name Foreign key
    ordering = ('-name',)  # сортировка по столбцу name от Я до А


# admin.site.register(Product)
# admin.site.register(ProductCategory)

