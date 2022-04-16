from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ModelViewSet

from . import models
from . import serialize
from luffy.utils.response import APIResponse
# Create your views here.


class BannerView(ModelViewSet):
    queryset = models.Banner.objects.filter(is_delete=False, is_show=True).order_by('display_order')
    serializer_class = serialize.BannerModelSerializer


class PythonCourseView(ModelViewSet):
    queryset = models.FreeCourse.objects.filter(is_delete=False, is_show=True).order_by('display_order')
    serializer_class = serialize.FreeCourseModelSerializer
