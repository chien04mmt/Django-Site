# from django.contrib.auth.models import User
from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver

from .models import Profile, User

_UNSAVED_IMAGEFIELD = 'unsaved_imagefield'

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(pre_save, sender=User)
def set_new_user_inactive(sender, instance, **kwargs):
    if instance._state.adding is True:
        instance.is_active = True
        instance.is_superuser = False
        instance.is_staff = False

@receiver(pre_save, sender=Profile)
def skip_saving_file(sender, instance, **kwargs):
    if not instance.pk and not hasattr(instance, _UNSAVED_IMAGEFIELD):
        setattr(instance, _UNSAVED_IMAGEFIELD, instance.avatar)
        instance.avatar = None

@receiver(post_save, sender=Profile)
def update_file_url(sender, instance, created, **kwargs):
    if created and hasattr(instance, _UNSAVED_IMAGEFIELD):
        instance.avatar = getattr(instance, _UNSAVED_IMAGEFIELD)
        instance.save()


@receiver(post_delete, sender=Profile)
def post_save_image(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    try:
        import os
        if os.path.basename(instance.avatar.path) != 'default.jpg':
            instance.avatar.delete(save=False)
    except:
        pass

@receiver(pre_save, sender=Profile)
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    try:
        old_img = instance.__class__.objects.get(id=instance.id).avatar.path
        try:
            new_img = instance.avatar.path
        except:
            new_img = None
        if new_img != old_img:
            import os
            if os.path.basename(old_img) != 'default.jpg':
                if os.path.exists(old_img):
                    os.remove(old_img)
    except:
        pass
