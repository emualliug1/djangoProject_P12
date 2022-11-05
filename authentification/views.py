from authentification.models import User, Team
from authentification.serializer import UserSerializer, TeamSerializer
from rest_framework.viewsets import ModelViewSet
from .permisssions import UserPermission, TeamPermission


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
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
