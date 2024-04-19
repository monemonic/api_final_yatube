from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Кастомная проверка разрешений на уровне объекта.
    Проверяет на авторство и аутентифицированность пользователя
    отправляющего запрос.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class IsUserOrReadOnly(permissions.IsAuthenticated):
    """
    Кастомная проверка разрешений на уровне объекта.
    Проверяет на авторство и аутентифицированность пользователя
    отправляющего запрос.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
