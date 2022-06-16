# from time import sleep
# from unicodedata import name
from django.test import TestCase
from . models import Business
# Create your tests here.


class ModelTesting(TestCase):
    def setUp(self):
        self.api = Business.objects.create(name='django', owner_info='django', address='django', employee_size=50)

    def test_post_model(self):
        d = self.api
        self.assertTrue(isinstance(d, Business))
        self.assertEqual(str(d), 'django')
