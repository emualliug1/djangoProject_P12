from rest_framework.permissions import BasePermission
from api.models import Client, Contract, Event
from authentification.models import User, Team
from django.shortcuts import get_object_or_404
from rest_framework import permissions


def in_team(user):
    team = ['GESTION', 'VENTE', 'SUPPORT']
    if str(user.team) in team:
        return True
    return False


def in_team_lead(user):
    team_lead = ['GESTION', 'VENTE']
    if str(user.team) in team_lead:
        return True
    return False


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
        if str(request.user.team) == 'Support':
            return request.method in permissions.SAFE_METHODS
        return in_team_lead(request.user)

    def has_object_permission(self, request, view, obj):
        details = ['update', 'destroy']
        if view.action in details:
            return request.user == obj.sales_contact


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
        if str(request.user.team) == 'Support':
            return request.method in permissions.SAFE_METHODS
        return in_team_lead(request.user)

    def has_object_permission(self, request, view, obj):
        details = ['update', 'destroy']
        if view.action in details:
            return request.user == obj.sales_contact


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
        if str(request.user.team) == 'Support':
            return request.method in permissions.SAFE_METHODS
        return in_team_lead(request.user)

    def has_object_permission(self, request, view, obj):
        details = ['update', 'destroy']
        if view.action in details:
            return request.user == obj.support_contact
