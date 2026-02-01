from django.db import models
from core.models import Requerment
from django.utils.text import slugify
class Category(Requerment):
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(unique=True,blank=True,editable=False)
    description = models.TextField(blank=True,null=True)
    def __str__(self):
        return f'{self.name} - {self.description}'
    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.name}')
        super().save(*args, **kwargs)
