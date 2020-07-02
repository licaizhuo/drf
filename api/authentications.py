from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

from api.models import User


class MyAuth(BaseAuthentication):
    def authenticate(self, request):
        auth = request.META.get('HTTP_AUTHORIZATION', None)
        if auth is None:
            return None
        auth_list = auth.split('-')
        if not (auth_list[0].lower() == "auth" and len(auth_list) == 2):
            raise exceptions.AuthenticationFailed("认证失败，信息有误")
        if auth_list[1] != "lcz123":
            raise exceptions.AuthenticationFailed("用户信息校验失败")
        user = User.objects.filter(username="lcz").first()
        if not user:
            raise exceptions.AuthenticationFailed("用户不存在")
        tup = (user, None)
        return tup
