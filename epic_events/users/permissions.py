from rest_framework import permissions
from rest_framework.permissions import DjangoModelPermissions, BasePermission


class ActualDjangoModelPermissions(DjangoModelPermissions):

    def __init__(self):
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']
        self.perms_map['HEAD'] = ['%(app_label)s.view_%(model_name)s']
        self.perms_map['OPTIONS'] = ['%(app_label)s.view_%(model_name)s']


class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in ["PUT", "PATCH"]:
            return True
        return request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        if request.user == obj:
            return True
        return request.method in permissions.SAFE_METHODS


class GroupPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS