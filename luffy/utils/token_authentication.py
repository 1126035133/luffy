import jwt

from rest_framework import exceptions
from rest_framework_jwt.utils import jwt_decode_handler
from rest_framework_jwt.authentication import BaseJSONWebTokenAuthentication
# from rest_framework_jwt.authentication


class TokenAuthentication(BaseJSONWebTokenAuthentication):

    def authenticate(self, request):
        jwt_value = request.META.get('HTTP_AUTHORIZATION')
        if jwt_value:
            try:
                payload = jwt_decode_handler(jwt_value)
            except jwt.ExpiredSignature:
                raise exceptions.AuthenticationFailed('签名已过期')
            except jwt.DecodeError:
                raise exceptions.AuthenticationFailed('签名错误')
            except jwt.InvalidTokenError:
                raise exceptions.AuthenticationFailed('签名不合法')

            user = self.authenticate_credentials(payload)

            return user, jwt_value
        raise exceptions.AuthenticationFailed('你没有携带认证参数')