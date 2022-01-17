from rest_framework.permissions import DjangoModelPermissions, BasePermission


class ActualDjangoModelPermissions(DjangoModelPermissions):

    def __init__(self):
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']
        self.perms_map['HEAD'] = ['%(app_label)s.view_%(model_name)s']
        self.perms_map['OPTIONS'] = ['%(app_label)s.view_%(model_name)s']

class CustomerPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(
                name__iexact="sales").exists() and obj.sales_contact != request.user:
            return False
        return True