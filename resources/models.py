from django.db import models
from core.models import Requerment
from skills.models import Skill
from django.utils.text import slugify
from core.validators import blank_validator
from django.contrib.auth import get_user_model
from unidecode import unidecode
User = get_user_model()
class Resource(Requerment):
    class TypeChoices(models.TextChoices):
        VIDEO = 'Video', 'Video'
        ARTICLE = 'Article', 'Article'
        BOOK = 'Book', 'Book'
        Other = 'Other','Other'
    title = models.CharField(max_length=100,validators=[blank_validator])
    url = models.URLField()
    resource_type = models.CharField(max_length=100,choices=TypeChoices.choices)
    slug = models.SlugField(editable=False,unique=True,blank=True)
    skills = models.ManyToManyField(Skill,related_name='resources')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resources')
    def __str__(self):
        return f'{self.title}'
    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(f'{self.title} - {self.user.username}'))
        super().save(*args, **kwargs)
        
