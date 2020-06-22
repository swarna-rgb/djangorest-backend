from rest_framework import permissions

class IsOwnerorReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_authenticated and request.user.is_superuser

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user


#manager - superuser - view, create, update, delete access
#emplyee should have view access only
# class IsManagerorEmployee(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         print("usename", request.user.username, request.user.username)
#         if request.user.is_superuser:
#             return obj.owner ==  request.user