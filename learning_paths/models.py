from django.db import models
from core.models import Requerment
from django.utils.text import slugify
from skills.models import Skill
class LearningPath(Requerment):
    title = models.CharField(max_length=255,unique=True)
    slug = models.SlugField(unique=True, blank=True, editable=False)
    description = models.TextField()
    skills = models.ManyToManyField(Skill, related_name='learning_paths')
    def __str__(self):
        return f'{self.title} - {self.goal}'
    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.title}')
        super().save(*args, **kwargs)
