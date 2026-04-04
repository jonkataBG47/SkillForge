import threading

from celery import shared_task
from django.core.mail import send_mail

from SkillForge.settings import EMAIL_HOST_USER
def send_register_email(email, username):
    send_mail(
        'Registration Notification',
        f'Hello {username} and welcome to SkillForge! Your registration was successful.',
        EMAIL_HOST_USER,
        [email],
    )

def send_register_email_async(email, username):
    threading.Thread(
        target=send_register_email,
        args=(email, username),
        daemon=True
    ).start()