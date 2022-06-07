from django.shortcuts import render, redirect

from apps.cart.models import Cart, CartItem
from apps.cart.cart import Cart_ses
from .models import Product


def main_page(request):
    if 'name' in request.GET:
        products = Product.objects.filter(name__icontains=request.GET.get('name'))
    else:
        products = Product.objects.all().order_by('-pk')
    return render(request, 'main-page.html', locals())

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == "POST":
        data = request.POST
        pr_item = product.product_items.get(pk=int(data.get('product-id')))
        if request.user.is_authenticated:
            cart = Cart.objects.get(user=request.user.id)
            price = int(pr_item.price)
            total_price = 1 * price
            image = pr_item.image.url
            name = pr_item.name
            url = pr_item.product.id
            CartItem.objects.create(cart=cart, product=pr_item, price=price, total_price=total_price, image=image, url=url, name = name)
        else:
            cart = Cart_ses(request)
            cart.add(pr_item, int(data.get('quantity')))
    return render(request, 'product-detail.html', locals())
