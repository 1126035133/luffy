from django.urls import path, re_path, include
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register('banner', views.BannerView)
router.register('free_course', views.PythonCourseView)

urlpatterns = [
    path('', include(router.urls)),

]
