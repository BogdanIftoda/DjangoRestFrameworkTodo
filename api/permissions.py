from rest_framework import permissions
from django.contrib.auth.models import Group


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_superuser:
            return True

        return obj.owner == request.user
