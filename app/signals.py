from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver, Signal
from django.utils import timezone
from app.models import Product


@receiver(user_logged_in)
def create_user_profile(sender, request, user, **kwargs):
    user.last_login_time = timezone.now()
    user.save()


@receiver(pre_save, sender=Product)
def create_product(sender, instance, **kwargs):
    print(instance, 'has been created')


@receiver(post_delete, sender=Product)
def delete_product(sender, instance, **kwargs):
    print(instance, 'has been deleted')