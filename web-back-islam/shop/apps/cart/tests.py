from django.test import TestCase, Client


class CartTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_cart(self):
        response = self.client.get('/cart/')

        self.assertEqual(response.status_code, 200)
        print(response.context)