from decimal import Decimal
from django.conf import settings

from apps.products.models import ProductItem

class Cart_ses:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'id': product.id}
        self.cart[product_id]['quantity'] += quantity
        self.session.modified = True

    def put_quantity(self, product_id, quantity):
        self.cart[product_id]['quantity'] = quantity
        self.cart[product_id]['total_price'] = int(self.cart[product_id]['quantity'] * Decimal(self.cart[product_id]['price']))
        self.session.modified = True

    def remove(self, product_id):
        if product_id in self.cart:
            del self.cart[product_id]
            self.session.modified = True

    def __iter__(self):
        for item in self.cart.values():
            product = ProductItem.objects.get(pk=item['id'])
            item['price'] = int(product.price)
            item['total_price'] = int(Decimal(item['quantity']) * item['price'])
            item['image'] = product.image.url
            item['name'] = product.name
            item['url'] = product.product.id
            yield item

    def __len__(self):
        return sum((item['quantity'] for item in self.cart.values()))

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in
            self)

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True