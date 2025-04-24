from rest_framework import permissions

class IsAuthenticatedStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'student'

from rest_framework import permissions

class IsOwnerOrReadOnlyHomework(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return False

        return obj.student == request.user
