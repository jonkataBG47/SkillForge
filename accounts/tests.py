from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
user = get_user_model()
class TestView(TestCase):
    def test_register_view_login(self):
        response = self.client.post(
            reverse('registration'),
            {
                'username': 'test',
                'email': 'jorjanea@gmail.com',
                'password1': 'joan26112008',
                'password2': 'joan26112008',

            })
        self.assertTrue(response.wsgi_request.user.is_authenticated)
    def test_register_view_redirect(self):
        user.objects.create_user(username='test', email='jorjanea@gmail.com', password='joan26112008')
        self.client.login(username='test', password='joan26112008')
        response = self.client.get(reverse('registration'))
        self.assertRedirects(response, reverse('home'))
    # def test_delete_view_login(self):
    #     response = self.client.post(
    #         reverse('profile_delete'), )