from rest_framework import permissions

class CanCheckHomework(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['teacher', 'supervisor','admin','worker']

    def has_object_permission(self, request, view, obj):
        return request.user.role in ['teacher', 'supervisor','admin','worker']
