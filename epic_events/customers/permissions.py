from rest_framework import permissions


class CustomerPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.groups.filter(name="Sales").exists():
            return True
        if request.user.groups.filter(name="Support").exists():
            return request.method in permissions.SAFE_METHODS
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name="Sales").exists():
            if request.user == obj.sales_contact:
                return request.method in ["GET", "PUT", "PATCH", "OPTIONS", "HEAD","DELETE"]
            else:
                return request.method in permissions.SAFE_METHODS
        if request.user.groups.filter(name="Support").exists():
            return request.method in permissions.SAFE_METHODS
        return False