from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.IsAuthenticated):
    """
    Кастомная проверка разрешений на уровне объекта.
    Проверяет на авторство и аутентифицированность пользователя
    отправляющего запрос.
    """

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )


class ReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class IsUserOrReadOnly(permissions.IsAuthenticated):
    """
    Кастомная проверка разрешений на уровне объекта.
    Проверяет на авторство и аутентифицированность пользователя
    отправляющего запрос.
    """

    def has_object_permission(self, request, view, obj):
        return (obj.user == request.user)
