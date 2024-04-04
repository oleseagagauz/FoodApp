from django.contrib import admin
from .models import Product, Cart, CartItem


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'calories',
                    'protein',
                    'lipids',
                    'carbohydrates',
                    'water']

    search_fields = ['name']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'display_items',
                    'total_calories',
                    'total_protein',
                    'total_carbohydrates',
                    'total_lipids',
                    'total_water']

    search_fields = ['user__username']

    def get_item_count(self, obj):
        return obj.item_count()
    get_item_count.short_description = 'Item Count'

    def display_items(self, obj):
        return ', '.join([item.name for item in obj.items.all()])

    display_items.short_description = 'Items'  # Название поля в админке


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'cart', 'quantity']
    search_fields = ['product__name', 'cart__user__username']
