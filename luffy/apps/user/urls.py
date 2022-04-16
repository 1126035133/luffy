from rest_framework.routers import SimpleRouter
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('test/', views.TestLogin.as_view()),
    path('login/', views.LoginView.as_view({'post': 'login'})),
    path('signup/', views.SignUpView.as_view({'post': 'signup'})),

]
