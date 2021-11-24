from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name='имя',
        unique=True,
    )

    description = models.TextField(
        verbose_name='описание',
        blank=True,
    )

    created = models.DateTimeField(  # фиксируем время создания
        auto_now_add=True
    )

    updated = models.DateTimeField(  # фиксируем время последнего обновления
        auto_now=True
    )

    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE
    )

    name = models.CharField(
        verbose_name='имя продукта',
        max_length=128,
    )

    image = models.ImageField(
        upload_to='products_images',
        blank=True
    )

    short_desc = models.CharField(
        verbose_name='краткое описание',
        max_length=60,
        blank=True,
    )

    description = models.TextField(
        verbose_name='описание продукта',
        blank=True,
    )

    price = models.DecimalField(
        verbose_name='цена',
        max_digits=8,
        decimal_places=2,
        default=0
    )

    quantity = models.PositiveIntegerField(
        verbose_name='количество на складе',
        default=0
    )

    created = models.DateTimeField(
        auto_now_add=True
    )

    updated = models.DateTimeField(
        auto_now=True
    )

    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return f'{self.name} ({self.category.name})'

    class Meta:
        ordering = ['-updated']
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class Contact(models.Model):
    name = models.CharField(
        verbose_name='имя контакта',
        max_length=128,
    )

    city = models.CharField(
        verbose_name='название города',
        max_length=128,
    )

    phone = models.CharField(
        verbose_name='телефон',
        max_length=60,
    )

    email = models.CharField(
        verbose_name='электронная почта',
        max_length=60,
    )

    address = models.CharField(
        verbose_name='адрес',
        max_length=128,
    )

    def __str__(self):
        return self.name
