from django.test import TestCase
from highcharts.core.models import Euro


class TestGet(TestCase):

    def setUp(self):
        Euro.objects.create(date='2016-01-01', value=4.2)
        self.resp = self.client.get('/euro_json/')

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_mimetype(self):
        self.assertEqual('application/json', self.resp['Content-Type'])

    def test_contents(self):
        data = self.resp.json()
        self.assertIn('euro', data.keys())
        self.assertEqual(1, len(data['euro']))
        self.assertEqual('2016-01-01', data['euro'][0][0])
        self.assertEqual(4.2, data['euro'][0][1])
