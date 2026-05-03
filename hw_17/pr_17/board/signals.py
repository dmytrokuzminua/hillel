from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta

from .models import Ad


@receiver(post_save, sender=Ad)
def send_ad_created_email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'New Ad Created',
            f'Your ad "{instance.title}" has been created.',
            'from@example.com',
            [instance.user.email],
            fail_silently=True,
        )


@receiver(post_save, sender=Ad)
def deactivate_old_ads(sender, instance, **kwargs):
    if instance.created_at < timezone.now() - timedelta(days=30):
        if instance.is_active:
            instance.is_active = False
            instance.save()