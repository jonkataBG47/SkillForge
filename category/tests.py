from django.test import TestCase
from django.contrib.auth import get_user_model

from category.forms import FormCategory
from category.models import Category

User = get_user_model()
class TestForm(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', email='jorjan@gmail.com', password='joan12321232')
        self.category = Category.objects.create(name='tes', description='', user=self.user)
    def test_category_form_correct_values(self):
        form_data = {
            'name':'test',
            'description':'test',
        }
        form = FormCategory(data=form_data)
        self.assertTrue(form.is_valid())
    def test_category_form_incorrect_values(self):
        form_data = {
            'name':'',
            'description':'test',
        }
        form = FormCategory(data=form_data)
        self.assertFalse(form.is_valid())
    def test_category_slug_correct_values(self):
        self.assertTrue(self.category.slug)
        self.assertEqual(self.category.slug,'tes-test')
    def test_category_slug_incorrect_values(self):
        self.assertTrue(self.category.slug)
        self.assertNotEqual(self.category.slug,'test')
