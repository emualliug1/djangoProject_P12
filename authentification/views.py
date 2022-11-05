from authentification.models import User, Team
from authentification.serializer import UserListSerializer, UserDetailSerializer, TeamSerializer
from rest_framework.viewsets import ModelViewSet
from .permisssions import UserPermission, TeamPermission


class MultipleSerializerMixin:
    """
    Creation d'une Mixin pour afficher la vue liste ou detail
    """
    serializer_detail_class = None
    action = None

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.serializer_detail_class is not None:
            return self.serializer_detail_class
        return super().get_serializer_class()


class UserViewSet(MultipleSerializerMixin, ModelViewSet):
    serializer_class = UserListSerializer
    serializer_detail_class = UserDetailSerializer
    permission_classes = [UserPermission]
    queryset = User.objects.all()

    def get_queryset(self):
        return self.queryset


class TeamViewSet(ModelViewSet):
    serializer_class = TeamSerializer
    permission_classes = [TeamPermission]
    queryset = Team.objects.all()

    def get_queryset(self):
        return self.queryset
