from rest_framework import serializers
from api.models import Client, Contract, Event
from authentification.serializer import UserSerializer


class ClientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'mobile', 'company_name', 'sales_contact']


class ClientDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'mobile', 'company_name', 'sales_contact']


class ContractListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ['id', 'client', 'contract_status', 'amount', 'payment_due', 'sales_contact', 'support_contact']

    def to_representation(self, instance):
        self.fields['client'] = ClientListSerializer(read_only=True)
        self.fields['sales_contact'] = UserSerializer(read_only=True)
        return super().to_representation(instance)


class ContractDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ['id', 'client', 'contract_status', 'amount', 'payment_due', 'sales_contact', 'support_contact']

    def to_representation(self, instance):
        self.fields['client'] = ClientListSerializer(read_only=True)
        return super().to_representation(instance)


class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'location', 'contract', 'event_status', 'attendees', 'event_date', 'notes']

    def to_representation(self, instance):
        self.fields['contract'] = ContractListSerializer(read_only=True)
        return super().to_representation(instance)


class EventDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'location', 'contract', 'event_status', 'attendees', 'event_date', 'notes']


