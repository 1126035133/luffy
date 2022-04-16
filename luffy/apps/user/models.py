from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    icon = models.ImageField(upload_to='icon', default='icon/default.png')
    telephone = models.CharField(max_length=11)

    class Meta:

        verbose_name = '用户表'
        db_table = 'luffy_user'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username