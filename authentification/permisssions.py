from rest_framework.permissions import BasePermission
from rest_framework import permissions

GESTION = 'Gestion'
SUPPORT = 'Support'
VENTE = 'Vente'


class UserPermission(BasePermission):
    """
    Permission de la classe User :
    GESTION : Les membres de l'équipe gestion ont tous les droits possibles.
    Liste :
        VENTE : Accès en lecture seule.
        SUPPORT : Accès en lecture seule.
    Détails :
        VENTE : Accès en lecture seule.
        SUPPORT : Accès en lecture seule.
    """
    message = "Vous n'avez pas la permission d'effectuer cette action"

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        elif str(request.user.team) == SUPPORT:
            return request.method in permissions.SAFE_METHODS
        elif str(request.user.team) == VENTE:
            return request.method in permissions.SAFE_METHODS
        elif str(request.user.team) == GESTION:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        details = ['retrieve', 'update', 'partial_update', 'destroy']
        if view.action in details:
            if request.user.is_superuser:
                return True
            elif str(request.user.team) == GESTION:
                return True
        return False


class TeamPermission(BasePermission):
    """
    Permission de la classe Team :
    GESTION : Les membres de l'équipe gestion ont tous les droits possibles.
    Liste :
        VENTE : Accès en lecture seule.
        SUPPORT : Accès en lecture seule.
    Détails :
        VENTE : Accès en lecture seule.
        SUPPORT : Accès en lecture seule.
    """
    message = "Vous n'avez pas la permission d'effectuer cette action"

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        elif str(request.user.team) == SUPPORT:
            return request.method in permissions.SAFE_METHODS
        elif str(request.user.team) == VENTE:
            return request.method in permissions.SAFE_METHODS
        elif str(request.user.team) == GESTION:
            return request.method in permissions.SAFE_METHODS
        return False
