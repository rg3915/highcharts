from django.test import TestCase
from highcharts.core.models import Dollar


class TestGet(TestCase):

    def setUp(self):
        Dollar.objects.create(date='2016-01-01', value=4.2)
        self.resp = self.client.get('/dollar_json/')

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_mimetype(self):
        self.assertEqual('application/json', self.resp['Content-Type'])

    def test_contents(self):
        data = self.resp.json()
        self.assertIn('dollar', data.keys())
        self.assertEqual(1, len(data['dollar']))
        self.assertEqual('2016-01-01', data['dollar'][0]['dia'])
        self.assertEqual(4.2, data['dollar'][0]['valor'])
