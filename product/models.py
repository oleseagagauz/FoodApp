from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from decimal import Decimal, ROUND_DOWN


# Create your models here.
class Product(models.Model):
    # per 100g
    name = models.CharField(max_length=30)
    calories = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(900)])
    protein = models.DecimalField(max_digits=5,
                                  decimal_places=1,
                                  validators=[MinValueValidator(0), MaxValueValidator(100)])
    lipids = models.DecimalField(max_digits=5,
                                 decimal_places=1,
                                 validators=[MinValueValidator(0), MaxValueValidator(100)])
    carbohydrates = models.DecimalField(max_digits=5,
                                        decimal_places=1,
                                        validators=[MinValueValidator(0), MaxValueValidator(100)])
    water = models.DecimalField(max_digits=5,
                                decimal_places=1,
                                validators=[MinValueValidator(0), MaxValueValidator(100)],
                                default=0)
    img = models.ImageField(upload_to='images/', default="images/img.png")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Продукты'
        verbose_name = 'Продукт'


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField('Product', through='CartItem')
    total_calories = models.DecimalField(max_digits=8, decimal_places=1, default=0)
    total_protein = models.DecimalField(max_digits=8, decimal_places=1, default=0)
    total_carbohydrates = models.DecimalField(max_digits=8, decimal_places=1, default=0)
    total_lipids = models.DecimalField(max_digits=8, decimal_places=1, default=0)
    total_water = models.DecimalField(max_digits=8, decimal_places=1, default=0)

    def update_totals(self):
        self.total_calories = Decimal(sum(
            Decimal(item.product.calories) * Decimal(item.quantity or 0) / 100 for item in
            self.cartitem_set.all())).quantize(
            Decimal('0.0'), rounding=ROUND_DOWN)
        self.total_protein = Decimal(sum(
            Decimal(item.product.protein) * Decimal(item.quantity or 0) / 100 for item in
            self.cartitem_set.all())).quantize(
            Decimal('0.0'), rounding=ROUND_DOWN)
        self.total_carbohydrates = Decimal(sum(
            Decimal(item.product.carbohydrates) * Decimal(item.quantity or 0) / 100 for item in
            self.cartitem_set.all())).quantize(Decimal('0.0'), rounding=ROUND_DOWN)
        self.total_lipids = Decimal(sum(
            Decimal(item.product.lipids) * Decimal(item.quantity or 0) / 100 for item in
            self.cartitem_set.all())).quantize(
            Decimal('0.0'), rounding=ROUND_DOWN)
        self.total_water = Decimal(sum(
            Decimal(item.product.water) * Decimal(item.quantity or 0) / 100 for item in
            self.cartitem_set.all())).quantize(
            Decimal('0.0'), rounding=ROUND_DOWN)
        self.save()

    def __str__(self):
        return f'Cart of {self.user.username}, {self.items.count()}'

    class Meta:
        verbose_name_plural = 'Корзины'
        verbose_name = 'Корзина'


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.cart.update_totals()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.cart.update_totals()

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in cart"

    class Meta:
        verbose_name_plural = 'Элементы корзины'
        verbose_name = 'Элемент корзины'
