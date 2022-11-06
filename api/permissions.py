from rest_framework.permissions import BasePermission
from rest_framework import permissions
from api.models import Client, Contract
from django.shortcuts import get_object_or_404

GESTION = 'Gestion'
SUPPORT = 'Support'
VENTE = 'Vente'


class ClientPermission(BasePermission):
    """
    Permission de la classe Client :
    GESTION : Les membres de l'équipe gestion ont tous les droits possibles.
    Liste :
        VENTE : Accès en lecture + création de nouveau client.
        SUPPORT : Accès en lecture seule.
    Détails :
        VENTE : Accès en lecture. Seule le créateur du client peut modifier ou le supprimer.
        SUPPORT : Accès en lecture seule.
    """
    message = "Vous n'avez pas la permission d'effectuer cette action"

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        elif str(request.user.team) == SUPPORT:
            return request.method in permissions.SAFE_METHODS
        elif str(request.user.team) == VENTE:
            return True
        elif str(request.user.team) == GESTION:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        details = ['retrieve', 'update', 'partial_update', 'destroy']
        if view.action in details:
            if request.user.is_superuser:
                return True
            elif request.user == obj.sales_contact:
                return True
            elif str(request.user.team) == GESTION:
                return True
            return False


class ContractPermission(BasePermission):
    """
    Permission de la classe Contract :
    GESTION : Les membres de l'équipe gestion ont tous les droits possibles.
    Liste :
        VENTE : Accès en lecture + création de nouveau contrat.
        SUPPORT : Accès en lecture seule.
    Détails :
        VENTE : Accès en lecture. Seule le créateur du contrat peut modifier ou le supprimer.
        SUPPORT : Accès en lecture seule.
    """
    message = "Vous n'avez pas la permission d'effectuer cette action"

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        elif str(request.user.team) == SUPPORT:
            return request.method in permissions.SAFE_METHODS
        elif str(request.user.team) == VENTE:
            return True
        elif str(request.user.team) == GESTION:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        client = get_object_or_404(Client, pk=view.kwargs['client_pk'])
        details = ['retrieve', 'update', 'partial_update', 'destroy']
        if view.action in details:
            if request.user.is_superuser:
                return True
            elif request.user == client.sales_contact:
                return True
            elif str(request.user.team) == GESTION:
                return True
        return False


class EventPermission(BasePermission):
    """
    Permission de la classe Event :
    GESTION : Les membres de l'équipe gestion ont tous les droits possibles.
    Liste :
        VENTE : Accès en lecture + création de nouveau event.
        SUPPORT : Accès en lecture seule.
    Détails :
        VENTE : Accès en lecture. Seule le créateur du contrat peut modifier ou le supprimer.
        SUPPORT : Accès en lecture seule. Seule le membre de l'équipe support désigné pour cette event peut le modifier.
    """
    message = "Vous n'avez pas la permission d'effectuer cette action"

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        elif str(request.user.team) == SUPPORT:
            return request.method in permissions.SAFE_METHODS
        elif str(request.user.team) == VENTE:
            return True
        elif str(request.user.team) == GESTION:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        contrat = get_object_or_404(Contract, pk=view.kwargs['contract_pk'])
        details = ['retrieve', 'update', 'partial_update', 'destroy']
        if view.action in details:
            if request.user.is_superuser:
                return True
            elif request.user == contrat.support_contact:
                if request.method == "PUT":
                    return True
                elif request.method == "PATCH":
                    return True
                elif request.method == "DELETE":
                    return False
            elif str(request.user.team) == GESTION:
                return True
        return False
