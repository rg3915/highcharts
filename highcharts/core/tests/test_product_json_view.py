from django.test import TestCase
from highcharts.core.models import Category, Product


class TestGet(TestCase):

    def setUp(self):
        category = Category.objects.create(category='Papelaria')
        Product.objects.create(
            product='A4',
            price=4.2,
            category=category
        )
        self.resp = self.client.get('/product_json/')

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_mimetype(self):
        self.assertEqual('application/json', self.resp['Content-Type'])


    def test_contents(self):
        data = self.resp.json()
        self.assertIn('products', data.keys())
        self.assertEqual(1, len(data['products']))
        self.assertEqual('Papelaria', data['products'][0]['categoria'])
        self.assertEqual(100.0, data['products'][0]['porcentagem'])
