from django.contrib import admin
from api.models import Client, Contract, Event


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'company_name')


class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'contract_status')


class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'event_status')


admin.site.register(Client, ClientAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Event, EventAdmin)
