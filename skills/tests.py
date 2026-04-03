from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse

from category.models import Category
from skills.forms import FormSkill
from skills.models import Skill
from skills.views import SkillListView

User = get_user_model()
class TestSkill(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', email='djswas@gmail.com', password='joaw23142312')
        self.user1 = User.objects.create_user(username='tes', email='djswa@gmail.com', password='joaw23142312')
        self.category = Category.objects.create(name='test',description='test',user=self.user)
        self.category1 = Category.objects.create(name='test', description='test', user=self.user1)
    def test_estimated_hours_min_value(self):
        skill = Skill.objects.create(title='test',description='test',difficulty = 'Beginner',estimated_hours = 0,category=self.category,user=self.user)
        with self.assertRaises(ValidationError) as e:
            skill.full_clean()
        self.assertIn('The estimated hours must be 1 or more', str(e.exception))
    def test_slug_generation(self):
        skill = Skill.objects.create(title='tes',description='test',difficulty = 'Beginner',estimated_hours = 0,category=self.category,user=self.user)
        self.assertTrue(skill.slug)
        self.assertEqual(skill.slug,'tes-test')
    def test_skill_presentation(self):
        skill = Skill.objects.create(title='test',description='test',difficulty = 'Beginner',estimated_hours = 1,category=self.category,user=self.user)
        skill1 = Skill.objects.create(title='tes',description='test',difficulty = 'Beginner',estimated_hours = 1,category=self.category1,user=self.user1)
        request = HttpRequest()
        request.user = self.user
        view = SkillListView()
        view.request = request
        # self.client.login(username='test', password='joaw23142312')
        # response = self.client.get(reverse('skill_list'))
        skills = view.get_queryset()
        self.assertIn(skill, skills)
        self.assertNotIn(skill1, skills)
    def test_category_form_correct_values(self):
        values = {
            'title':'test',
            'description':'test',
            'difficulty':'Beginner',
            'estimated_hours':1,
            'category':self.category,
        }
        form = FormSkill(data=values)
        self.assertTrue(form.is_valid())
    def test_category_form_incorrect_values(self):
        values = {
            'title':'',
            'description':'',
            'difficulty':'Beginner',
            'estimated_hours':1,
            'category':self.category,
        }
        form = FormSkill(data=values)
        self.assertFalse(form.is_valid())


