from django.db import models
from core.models import Requerment
from skills.models import Skill
from django.utils.text import slugify
from core.validators import blank_validator
class Resource(Requerment):
    class TypeChoices(models.TextChoices):
        VIDEO = 'Video', 'Video'
        ARTICLE = 'Article', 'Article'
        BOOK = 'Book', 'Book'
        Other = 'Other','Other'
    title = models.CharField(max_length=100,unique=True,validators=[blank_validator])
    url = models.URLField()
    resource_type = models.CharField(max_length=100,choices=TypeChoices.choices)
    slug = models.SlugField(editable=False,unique=True,blank=True)
    skills = models.ManyToManyField(Skill,related_name='resources')
    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.title} - {self.resource_type}')
        super().save(*args, **kwargs)
        
