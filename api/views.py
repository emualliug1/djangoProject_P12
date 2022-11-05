from api.models import Client, Contract, Event
from api.serializer import ClientListSerializer, ClientDetailSerializer
from api.serializer import ContractListSerializer, ContractDetailSerializer
from api.serializer import EventListSerializer, EventDetailSerializer
from rest_framework.viewsets import ModelViewSet
from .permissions import ClientPermission, ContractPermission, EventPermission


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


class ClientViewSet(MultipleSerializerMixin, ModelViewSet):
    """
    ViewSet des Clients
    """
    serializer_class = ClientListSerializer
    serializer_detail_class = ClientDetailSerializer
    permission_classes = [ClientPermission]
    queryset = Client.objects.all()

    def get_queryset(self):
        return self.queryset

    def perform_create(self, serializer):
        serializer.save(sales_contact=self.request.user)


class ContractViewSet(MultipleSerializerMixin, ModelViewSet):
    """
    ViewSet des Contracts
    """

    serializer_class = ContractListSerializer
    serializer_detail_class = ContractDetailSerializer
    permission_classes = [ContractPermission]
    queryset = Contract.objects.all()

    def get_queryset(self):
        client_pk = self.kwargs['client_pk']
        return self.queryset.filter(client=client_pk)

    def perform_create(self, serializer):
        serializer.save(client=Client.objects.get(id=self.kwargs['client_pk']),
                        sales_contact=self.request.user)


class EventViewSet(MultipleSerializerMixin, ModelViewSet):
    """
    ViewSet des Events
    """

    serializer_class = EventListSerializer
    serializer_detail_class = EventDetailSerializer
    permission_classes = [EventPermission]
    queryset = Event.objects.all()

    def get_queryset(self):
        contract_pk = self.kwargs['contract_pk']
        return self.queryset.filter(contract=contract_pk)
