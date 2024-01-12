"""Модуль разрешений и доступов."""
from rest_framework import permissions


class IsAuthorOrReadOnlyPermission(permissions.BasePermission):
    """Класс для проверки на авторство."""

    def has_object_permission(self, request, view, obj):
        """Получение имени автора."""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
