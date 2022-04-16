from django.db import models
from luffy.utils.models import BaseModel
# Create your models here.
from django.contrib import auth


class Banner(BaseModel):
    name = models.CharField(max_length=24)
    img = models.ImageField(upload_to='banner', verbose_name='轮播图', help_text='图片尺寸：3840*800')
    link = models.CharField(max_length=64, verbose_name='跳转链接')
    info = models.TextField()

    class Meta:
        verbose_name = '广告表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class FreeCourse(BaseModel):
    title = models.CharField(max_length=64)
    img = models.ImageField(upload_to='free_course', verbose_name='免费课图', help_text='图片尺寸：768*434')
    link = models.CharField(max_length=64, verbose_name='跳转链接')
    info = models.TextField()

    class Meta:
        verbose_name = '免费课表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
