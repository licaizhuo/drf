from django.contrib.auth.models import Group, Permission
from django.shortcuts import render
from rest_framework.request import Request
from rest_framework import settings
from rest_framework import permissions
# Create your views here.
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView

from api.authentications import MyAuth
from api.models import User
from api.permissions import MyPermission
from utils.response import MyResponse


class TestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        # user = User.objects.first()
        # print(user)
        # print(user.groups.first(), type(user.groups.first()))
        # print(user.groups.first().name, type(user.groups.first().name))
        # print(user.user_permissions.all().first().name)

        # group = Group.objects.first()
        # print(group)
        # print(group.permissions.first().name)
        # print(group.user_set.first().username)
        # print(group.user_set.all().values('username'))

        # permission = Permission.objects.filter(pk=4).first()
        # print(permission.user_set.first().username)
        # per = Permission.objects.filter(pk=8).first()
        # print(per.group_set.first().name)
        return MyResponse(data_message="查询成功")


class TestPermissionAPIView(APIView):
    authentication_classes = [MyAuth]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return MyResponse(data_message="登录访问成功")


class UserLoginOrReadOnly(APIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [MyPermission]
    throttle_classes = [UserRateThrottle]

    def get(self, request, *args, **kwargs):
        return MyResponse(data_message="浏览页面打开成功")

    def post(self, request, *args, **kwargs):
        return MyResponse(data_message="修改成功")


class SendMessageAPIView(APIView):
    throttle_classes = [SendMessageRate]

    def get(self, request, *args, **kwargs):
        return APIResponse("读操作访问成功")

    def post(self, request, *args, **kwargs):
        return APIResponse("写操作")
