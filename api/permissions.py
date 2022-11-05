from rest_framework.permissions import BasePermission
from rest_framework import permissions
from api.models import Client, Contract, Event
from django.shortcuts import get_object_or_404

GESTION = 'Gestion'
SUPPORT = 'Support'
VENTE = 'Vente'


class ClientPermission(BasePermission):
    """
    Permission de classe Client :
    GESTION TEAM : les membres de l'équipe de gestion ont tous les droits possibles
    Liste :
        VENTE TEAM : creer un nouveau client
        SUPPORT TEAM : seul la lecture cette vue est possible
    Détails :
        VENTE TEAM : seul l'auteur de cette vue peux la modifier ou la supprimer
        SUPPORT TEAM : seul la lecture cette vue est possible
    """
    message = "Vous n'avez pas la permission d'effectuer cette action"

    def has_permission(self, request, view):
        if str(request.user.team) == SUPPORT:
            return request.method in permissions.SAFE_METHODS
        elif str(request.user.team) == VENTE or GESTION:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        details = ['retrieve', 'update', 'partial_update', 'destroy']
        if view.action in details:
            if request.user == obj.sales_contact:
                return True
            if str(request.user.team) == GESTION:
                return True
            return False


class ContractPermission(BasePermission):
    """
    Permission de classe Client :
    GESTION TEAM : les membres de l'équipe de gestion ont tous les droits possibles
    Liste :
        VENTE TEAM : creer un nouveau contrat
        SUPPORT TEAM : seul la lecture cette vue est possible
    Détails :
        VENTE TEAM : seul l'auteur de cette vue peux la modifier ou la supprimer
        SUPPORT TEAM : seul la lecture cette vue est possible
    """
    message = "Vous n'avez pas la permission d'effectuer cette action"

    def has_permission(self, request, view):
        if str(request.user.team) == SUPPORT:
            return request.method in permissions.SAFE_METHODS
        elif str(request.user.team) == VENTE or GESTION:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        client = get_object_or_404(Client, pk=view.kwargs['client_pk'])
        details = ['retrieve', 'update', 'partial_update', 'destroy']
        if view.action in details:
            if request.user == client.sales_contact:
                return True
            if str(request.user.team) == GESTION:
                return True
        return False


class EventPermission(BasePermission):
    """
    Permission de classe Client :
    GESTION TEAM : les membres de l'équipe de gestion ont tous les droits possibles
    Liste :
        VENTE TEAM : creer un nouveau contrat
        SUPPORT TEAM : seul la lecture cette vue est possible
    Détails :
        VENTE TEAM : seul l'auteur de cette vue peux la modifier ou la supprimer
        SUPPORT TEAM : seul la lecture cette vue est possible
    """
    message = "Vous n'avez pas la permission d'effectuer cette action"

    def has_permission(self, request, view):
        if str(request.user.team) == SUPPORT:
            return request.method in permissions.SAFE_METHODS
        elif str(request.user.team) == VENTE or GESTION:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        contrat = get_object_or_404(Contract, pk=view.kwargs['contract_pk'])
        details = ['retrieve', 'update', 'partial_update', 'destroy']
        if view.action in details:
            if request.user == contrat.support_contact:
                return True
            if str(request.user.team) == GESTION:
                return True
        return False



