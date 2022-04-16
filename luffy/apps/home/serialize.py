from rest_framework import serializers
from .models import *


class BannerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ['name', 'link', 'img']


class FreeCourseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeCourse
        fields = ['title', 'link', 'img']