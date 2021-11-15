from django.db import models
from django.contrib.auth.models import AbstractUser


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст')
<<<<<<< HEAD
=======
    is_active = models.BooleanField(default=True)
>>>>>>> Lesson_7
