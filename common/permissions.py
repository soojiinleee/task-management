from rest_framework import permissions


class IsCreatorOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    """
    Custom permission to only allow creator of an object to edit it
    or is a read-only request.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.create_user == request.user


class IsTeamMemberOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    """
    Custom permission to only allow team member of an object to edit it
    or is a read-only request.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.team == request.user.team
