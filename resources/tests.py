from django.contrib.auth import get_user_model
from django.http import HttpRequest
from django.test import TestCase
from unittest.mock import patch, MagicMock

from django.urls import reverse

from category.models import Category
from skills.models import Skill
from resources.models import Resource
User = get_user_model()
class TestResource(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', email='hdsawsw2123@gmail.com', password='joan21212121')
        self.category = Category.objects.create(name='title',description = '',user = self.user)
        self.skill = Skill.objects.create(title='test',description='test',difficulty = 'Beginner',estimated_hours = 1,category=self.category,user=self.user)
        self.resource = Resource.objects.create(title='видео',url = 'https://mail.google.com/mail/u/0/#inbox',resource_type = 'Video',user = self.user)
        self.resource.skills.set([self.skill])
    def test_resource_slug(self):
        self.assertTrue(self.resource.slug)
        self.assertEqual(self.resource.slug,'video-test')

    def test_resource_model_fast(self):
        resource = MagicMock()
        resource.title = 'video'
        resource.slug = 'video-test'

        self.assertEqual(resource.slug, 'video-test')


