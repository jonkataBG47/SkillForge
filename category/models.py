from django.db import models
from core.models import Requerment
from django.utils.text import slugify
from core.validators import blank_validator
from django.contrib.auth import get_user_model
from unidecode import unidecode
User = get_user_model()
class Category(Requerment):
    name = models.CharField(max_length=100,unique=True,validators=[blank_validator])
    slug = models.SlugField(unique=True,blank=True,editable=False)
    description = models.TextField(blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='category')
    def __str__(self):
        return f'{self.name}'
    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(f'{self.name} - {self.user.username}'))
        super().save(*args, **kwargs)
