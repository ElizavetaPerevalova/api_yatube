from rest_framework import permissions


class isAuthorOrAuthenticated(permissions.BasePermission):
    """Управление правами доступа."""
    def has_permission(self, request, view,):
        """Этот метод возвращает True, если пользователь аутентифицирован,
        и False в противном случае."""
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """Проверка разрешений на уровне экземпляра.
        Этот метод должен возвращать значение True или False."""
        if request.method in ('GET', 'POST'):
            return request.user.is_authenticated
        if request.method in ('PATCH', 'PUT', 'DELETE'):
            return request.user.is_authenticated and obj.author == request.user
