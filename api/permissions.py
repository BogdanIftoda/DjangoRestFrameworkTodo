from rest_framework import permissions
from django.contrib.auth.models import Group


class IsAuthorOrReadOnly(permissions.BasePermission):

    # group_name = "Admin"

    def has_object_permission(self, request, view, obj):
        # if request.user and request.user.is_authenticated:
        #     if request.method in permissions.SAFE_METHODS and request.user and request.user.groups.filter(name=self.group_name):
        #         if obj.owner.groups.filter(name=self.group_name):
        #             return True
        #         return False

        if request.user and request.user.is_superuser:
            return True

        return obj.owner == request.user
