from django.db import models
from core.models import Requerment
from django.utils.text import slugify
from skills.models import Skill
from core.validators import blank_validator
class LearningPath(Requerment):
    title = models.CharField(max_length=255,unique=True,validators=[blank_validator])
    slug = models.SlugField(unique=True, blank=True, editable=False)
    description = models.TextField(validators=[blank_validator])
    skills = models.ManyToManyField(Skill, related_name='learning_paths')
    def __str__(self):
        return f'{self.title} - {self.description}'
    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.title}')
        super().save(*args, **kwargs)
