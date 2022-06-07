from django.shortcuts import render
from django.http import JsonResponse

from .models import Cart, CartItem
from .cart import Cart_ses 
from apps.products.models import ProductItem


def cart_detail(request):
    if request.user.is_authenticated:
        cart = Cart.objects.get(user=request.user.id).cart_items.all()
    else:
        cart = Cart_ses(request)
    return render(request, 'cart-detail.html', locals())

def change_quantity(request):
    quantity = int(request.GET.get('quantity'))
    price = ProductItem.objects.get(pk=int(request.GET.get('id')[8:])).price    
    date = {'total_price': price*quantity}
    return JsonResponse(date)

def item_ad(request):
    print(request.POST)
    if request.POST.get('remove'):
        if request.user.is_authenticated:
            cart = Cart.objects.get(user=request.user.id)
        else:
            cart = Cart(request)
            cart.remove(request.POST.get('id'))
        return JsonResponse({'status': '200'})