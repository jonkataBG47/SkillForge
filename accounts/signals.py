from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import SkillForgeUser
from accounts.tasks import send_register_email

# @receiver(post_save, sender=SkillForgeUser)
# def send_welcome_email(sender, instance, created, **kwargs):
#     if created:
#         send_register_email.delay(instance.email, instance.username)
