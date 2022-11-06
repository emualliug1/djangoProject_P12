from authentification.models import User, Team
from rest_framework import serializers


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'team']
        read_only_fields = ['id', 'username']


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'team']


class TeamSerializer(serializers.ModelSerializer):
    users = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Team
        fields = ['team', 'users']

    def get_users(self, instance):
        queryset = instance.users.all()
        serializer = UserListSerializer(queryset, many=True)
        return serializer.data
