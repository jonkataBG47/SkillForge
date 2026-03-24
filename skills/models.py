from django.db import models
from core.models import Requerment
from django.utils.text import slugify
from django.core.validators import MinValueValidator
from category.models import Category
from core.validators import blank_validator
from django.contrib.auth import get_user_model
from unidecode import unidecode
User = get_user_model()
class Skill(Requerment):
    class SkillChoices(models.TextChoices):
        BEGINNER = 'Beginner','Beginner'
        INTERMEDIATE = 'Intermediate','Intermediate'
        ADVANCED = 'Advanced','Advanced'
    title = models.CharField(max_length=255,validators=[blank_validator])
    slug = models.SlugField(unique=True,blank=True,editable=False)
    description = models.TextField(validators=[blank_validator])
    difficulty = models.CharField(max_length=50,choices=SkillChoices.choices)
    estimated_hours = models.PositiveIntegerField(validators=[MinValueValidator(1,'The estimated hours must be 1 or more')])
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='skills')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='skills')

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(f'{self.title} - {self.user.username}'))
        super().save(*args, **kwargs)