from rest_framework.permissions import BasePermission

class IsCommentAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user or request.user.is_superuser == obj.user