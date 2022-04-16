from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import

from rest_framework_jwt.authentication import BaseJSONWebTokenAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.utils import jwt_response_payload_handler

from luffy.utils.response import APIResponse
from . import serialize
from . import models
# Create your views here.


from luffy.utils.token_authentication import TokenAuthentication
class TestLogin(APIView):
    # authentication_classes = [TokenAuthentication, ]
    # permission_classes = [IsAuthenticated]

    def get(self, request, *args):

        return APIResponse(result='测试页面 用户：%s' % self.request.user.username)


class LoginView(ViewSet):
    authentication_classes = []
    permission_classes = []
    # queryset = models.User.objects.filter(is_active=True)

    def login(self, request, *args, **kwargs):

        login_ser = serialize.LoginModelSerialize(data=request.data)

        login_ser.is_valid(raise_exception=True)
        token = login_ser.context.get('token')
        username = login_ser.context.get('username')
        return APIResponse(msg='登录成功', result={'token': token, 'username': username})


class SignUpView(ViewSet):
    authentication_classes = []
    permission_classes = []

    def signup(self, request, *args, **kwargs):

        signup_ser = serialize.SignUpSerialize(data=request.data)
        signup_ser.is_valid(raise_exception=True)
        request.data.pop('re_password')
        user = models.User.objects.create_user(**request.data)

        return APIResponse(msg='注册成功', result={'username': user.username, 'email': user.email, 'telephone': user.telephone})