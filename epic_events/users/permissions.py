from rest_framework import permissions


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