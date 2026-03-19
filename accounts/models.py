from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
class SkillForgeUser(AbstractUser):
    image = models.ImageField(upload_to='profile_images/', blank=True, default='profile_images/default_profile.jpg')
    phone_number = models.CharField(max_length=15, validators=[RegexValidator(regex=r'^\d{8,15}$', message="Phone number must be entered in the format: '088888888...'. Up to 15 digits allowed.")], blank=True, null=True)
    
