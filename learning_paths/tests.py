from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from category.models import Category
from skills.models import Skill
from learning_paths.models import LearningPath

User = get_user_model()


class TestLearningPaths(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test',
            email='test@example.com',
            password='joan21212121'
        )
        self.category = Category.objects.create(
            name='Programming',
            description='',
            user=self.user
        )
        self.skill = Skill.objects.create(
            title='Python Basics',
            description='intro',
            difficulty='Beginner',
            estimated_hours=5,
            category=self.category,
            user=self.user
        )
        self.path = LearningPath.objects.create(
            title='Python Roadmap',
            description='step by step',
            user=self.user
        )
        self.path.skills.set([self.skill])

    def test_learning_path_slug_is_generated_correctly(self):
        self.assertTrue(self.path.slug)
        self.assertEqual(self.path.slug, 'python-roadmap-test')

    def test_path_list_view_shows_user_paths(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('path_list'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'learning_paths/path_list.html')
        self.assertIn('paths', response.context)
        self.assertContains(response, 'Python Roadmap')
        self.assertEqual(list(response.context['paths']), [self.path])

