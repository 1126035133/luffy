import re

from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from rest_framework_jwt.utils import jwt_encode_handler, jwt_payload_handler
from rest_framework_jwt.authentication import get_authorization_header
from . import models
from rest_framework_jwt.utils import jwt_response_payload_handler


class LoginModelSerialize(serializers.ModelSerializer):
    username = serializers.CharField()

    class Meta:
        model = models.User
        fields = ['username', 'password']

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if re.match(r'^1(3\d|4[4-9]|5[0-35-9]|6[67]|7[013-8]|8[0-9]|9[0-9])\d{8}$',username):
            user = models.User.objects.filter(telephone=username).first()
        elif re.match(r'^.+@.+$', username):
            user = models.User.objects.filter(email=username).first()
        else:
            user = models.User.objects.filter(username=username).first()

        if user:
            if user.check_password(password):
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                self.context['token'] = token
                self.context['username'] = user.username
                return attrs
            else:
                raise ValidationError('密码错误')
        else:
            raise ValidationError('用户不存在')

from rest_framework.exceptions import ErrorDetail
class SignUpSerialize(serializers.ModelSerializer):
    re_password = serializers.CharField(write_only=True)

    class Meta:
        model = models.User
        fields = ['username', 'password', 'email', 'telephone', 're_password']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 3},
                        'username': {'write_only': True},
                        'telephone': {'write_only': True, 'required': False},
                        'email': {'write_only': True, 'required': False},}

    def validate(self, attrs):
        re_password = attrs.get('re_password')
        password = attrs.get('password')
        telephone = attrs.get('telephone')
        email = attrs.get('email')

        if re_password != password:
            raise ValidationError('输入的密码不一致')
        if telephone:
            user = models.User.objects.filter(telephone=telephone).first()
            if user:
                raise ValidationError('此手机号已绑定其他账号')
        elif email:
            user = models.User.objects.filter(email=email).first()
            if user:
                raise ValidationError('此邮箱号已绑定其他账号')
        return attrs
