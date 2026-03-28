from django.db import models
from core.models import Requerment
from django.utils.text import slugify
from skills.models import Skill
from core.validators import blank_validator
from django.contrib.auth import get_user_model
from unidecode import unidecode
User = get_user_model()
class LearningPath(Requerment):
    title = models.CharField(max_length=255,validators=[blank_validator])
    slug = models.SlugField(unique=True, blank=True, editable=False)
    description = models.TextField(validators=[blank_validator])
    skills = models.ManyToManyField(Skill, related_name='learning_paths')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='learning_paths')
    def __str__(self):
        return f'{self.title}'
    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(f'{self.title} - {self.user.username}'))
        super().save(*args, **kwargs)
