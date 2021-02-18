from rest_framework import permissions
from django.contrib.auth.models import Group


class IsAuthorOrReadOnly(permissions.BasePermission):

    group_name = "Admin"

    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True 

        elif request.user and request.user.groups.filter(name=self.group_name):
            if obj.owner.groups.filter(name=self.group_name):
                return True
            return False
        
        elif request.user and request.user.is_superuser:
            return True 
    
        return obj.owner == request.user
    

