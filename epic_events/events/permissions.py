from rest_framework import permissions


class EventPermission(permissions.BasePermission):

    def has_permission(self, request):
        if request.user.groups.filter(name="Sales").exists():
            return request.method in permissions.SAFE_METHODS
        if request.user.groups.filter(name="Support").exists():
            return request.method in [
                "GET", "PUT", "PATCH", "OPTIONS", "HEAD"]
        return False

    def has_object_permission(self, request, obj):
        if request.user.groups.filter(name="Sales").exists():
            return request.method in permissions.SAFE_METHODS
        if request.user.groups.filter(name="Support").exists():
            if (request.user == obj.support_contact and
                    obj.accomplish is False):
                return request.method in [
                    "GET", "PUT", "PATCH", "OPTIONS", "HEAD"]
            else:
                return request.method in permissions.SAFE_METHODS
        return False