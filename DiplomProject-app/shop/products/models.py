from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Категория устройства")
    description = models.TextField(blank=True, verbose_name="Описание категории устройста")
    time = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория устройства"
        verbose_name_plural = "Категории устройств"
        ordering = ['-time']

class Product(models.Model):
    name = models.CharField(max_length=300, verbose_name="Название")
    image = models.ImageField(upload_to='device_image/%Y', blank=True, verbose_name='Фото')
    description = models.TextField(max_length=1000, verbose_name='Описание')
    short_description = models.CharField(max_length=300, blank=True, verbose_name="Краткое описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Цена")
    quantity = models.IntegerField(default=0, verbose_name="Количество")
    time = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name="Категория")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-time']