from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from product.forms import AddToCartForm, RemoveFromCartForm
from product.models import Product, Cart, CartItem
from django.shortcuts import get_object_or_404


def add_to_cart(request):
    form = AddToCartForm(request.POST)
    if form.is_valid():
        quantity = form.cleaned_data['quantity']
        product_id = form.cleaned_data['product_id']
        try:
            product = get_object_or_404(Product, id=product_id)
        except Product.DoesNotExist:
            return HttpResponseBadRequest("Product does not exist")

        # Создаем или получаем корзину текущего пользователя
        cart, created = Cart.objects.get_or_create(user=request.user)

        # Создаем или обновляем элемент корзины с учетом указанного количества
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if cart_item.quantity is not None:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
        cart_item.save()


def remove_from_cart(request):
    form = RemoveFromCartForm(request.POST)
    if form.is_valid():
        product_id = form.cleaned_data['product_id']
        try:
            product = get_object_or_404(Product, id=product_id)
        except Product.DoesNotExist:
            return HttpResponseBadRequest("Product does not exist")

        # Получаем корзину текущего пользователя
        cart = Cart.objects.get(user=request.user)

        # Удаляем элемент корзины
        cart_item = CartItem.objects.get(cart=cart, product=product)
        cart_item.delete()


def product_list(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'remove':
            remove_from_cart(request)
        else:
            add_to_cart(request)
        return redirect(to='product:cart')  # Перенаправляем пользователя обратно на страницу продуктов
    else:
        form = AddToCartForm()

    products = Product.objects.all()
    return render(request, 'product/products.html', {'products': products, 'form': form})


def cart_view(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'remove':
            remove_from_cart(request)
        else:
            add_to_cart(request)
        return redirect(to='product:cart')  # Перенаправляем пользователя обратно на страницу продуктов
    else:
        form = AddToCartForm()
        try:
            user_cart = Cart.objects.get(user=request.user)
            cart_item = CartItem.objects.filter(cart=user_cart)
            return render(request, 'product/cart.html',
                          {"user_cart": user_cart,
                           "cart_item": cart_item,
                           "form": form})
        except Cart.DoesNotExist:
            return render(request, 'product/cart.html')
