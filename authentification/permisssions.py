from rest_framework.permissions import BasePermission
from rest_framework import permissions

GESTION = 'Gestion'
SUPPORT = 'Support'
VENTE = 'Vente'


class UserPermission(BasePermission):
    """
    Permission de classe User :
    GESTION TEAM : les membres de l'équipe de gestion ont tous les droits possibles
    Liste :
        VENTE TEAM : Read only
        SUPPORT TEAM : Read only
    Détails :
        VENTE TEAM : Read only
        SUPPORT TEAM : Read only
    """
    message = "Vous n'avez pas la permission d'effectuer cette action"

    def has_permission(self, request, view):
        if str(request.user.team) == SUPPORT:
            return request.method in permissions.SAFE_METHODS
        elif str(request.user.team) == VENTE:
            return request.method in permissions.SAFE_METHODS
        elif str(request.user.team) == GESTION:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        details = ['retrieve', 'update', 'partial_update', 'destroy']
        if view.action in details:
            if str(request.user.team) == GESTION:
                return True
        return False


class TeamPermission(BasePermission):
    """
    Permission de classe Client :
    GESTION TEAM : les membres de l'équipe de gestion ont tous les droits possibles
    Liste :
        VENTE TEAM : Read only
        SUPPORT TEAM : Read only
    Détails :
        VENTE TEAM : Read only
        SUPPORT TEAM : Read only
    """
    message = "Vous n'avez pas la permission d'effectuer cette action"

    def has_permission(self, request, view):
        if str(request.user.team) == SUPPORT:
            return request.method in permissions.SAFE_METHODS
        elif str(request.user.team) == VENTE:
            return request.method in permissions.SAFE_METHODS
        elif str(request.user.team) == GESTION:
            return request.method in permissions.SAFE_METHODS
        return False

