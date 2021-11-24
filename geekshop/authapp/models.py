from django.db import models
from django.contrib.auth.models import AbstractUser
import pytz
from datetime import datetime, timedelta
from django.conf import settings


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст')
    is_active = models.BooleanField(default=True)
<<<<<<< HEAD
    activate_key = models.CharField(max_length=128, verbose_name='Ключ активации', blank=True, null=True)
    activate_key_expired = models.DateTimeField(blank=True, null=True)

    def is_activate_key_expired(self):
        if datetime.now(pytz.timezone(settings.TIME_ZONE)) > self.activate_key_expired + timedelta(hours=48):
            return True
        return False

    def activate_user(self):
        self.is_active = True
        self.activate_key = None
        self.active_key_expired = None
        self.save()
=======
>>>>>>> bd709e49b3c3cbad21a990c65101e6b3c0f3c791
