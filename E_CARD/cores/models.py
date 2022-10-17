#models.py
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image


def upload_path_handler(instance, filename):
    import os.path
    fn, ext = os.path.splitext(filename)
    return "avatars/{id}/{fname}".format(id=instance.user, fname=filename)


class Profile(models.Model):
    user   = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to=upload_path_handler)
    theme = models.CharField(max_length=20, default='light-mode',blank=True,null=True)
    displayName = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{ self.user.username } Profile'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)
        # img.save(self.avatar.path)

        if img.height > 500 or img.width > 500:
            new_img = (500, 500)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

class User(AbstractUser):
    Location = models.CharField(max_length=200, blank=True, null=True)
    EmployeeID = models.CharField(max_length=200, blank=True, null=True)
