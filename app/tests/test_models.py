from django.test import TestCase
from..models import User, Product

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user(username='testuser', password='12345')
        self.assertEqual(user.username, 'testuser')

class ProductModelTest(TestCase):
    def test_product_creation(self):
        product = Product.objects.create(name='Test Product', description='Test Description', price=100.00)
        self.assertEqual(product.name, 'Test Product')