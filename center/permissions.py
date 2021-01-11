from rest_framework import permissions

class permissionsClass(permissions.BasePermission):
    def has_object_permission(self,request,view,obj):
        if request.user.id == 1:
            return True
        if request.method == 'DELETE' and request.user.id != 1:
            return False
        if request.user == obj.employee:
            return True
        if request.method in permissions.SAFE_METHODS:
            return True