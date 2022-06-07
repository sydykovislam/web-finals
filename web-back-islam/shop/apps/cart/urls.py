from django.urls import path

from .views import cart_detail, change_quantity,item_ad

urlpatterns = [
    path('', cart_detail, name='cart-detail'),
    path('change-quantity/', change_quantity, name='change-quantity'),
    path('item-ad/', item_ad, name='card-item-ad')
]