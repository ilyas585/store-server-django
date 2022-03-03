from django.db import models
# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    # description не объязательно к заполнению, если пустое значит ставим NULL в БД
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='products_images')
    description = models.CharField(max_length=128)
    # до запятой max_digits цифр, после запятой decimal_places цифр
    price = models.DecimalField(max_digits=8, decimal_places=2)
    # изначально количество товаров равно 0,
    # тип PositiveSmallIntegerField означает число может быть только больше нуля
    quantity = models.PositiveSmallIntegerField(default=0)
    # ForeignKey - внешний ключ, поле category связываем с полем id ProductCategory
    # если удаляется категория из модели ProductCategory, то
    # каскадно удаляются все строки где использовалась данная категория
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'Продукт {self.name} | Категория {self.category.name}'
