from rest_framework import permissions

from api.models import User


class MyPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        username = request.data.get("username")
        user = User.objects.filter(username=username).first()
        if user:
            return True
        return False
