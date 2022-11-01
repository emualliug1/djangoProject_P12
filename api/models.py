from django.db import models
from authentification.models import User


class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    mobile = models.CharField(max_length=30, blank=True, null=True)
    company_name = models.CharField(max_length=250, blank=True, null=True)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now=True)
    sales_contact = models.ForeignKey(User,
                                      on_delete=models.SET_NULL,
                                      null=True,
                                      blank=True,
                                      limit_choices_to={"team_id": 0})

    def __str__(self):
        client = f"{self.first_name} {self.last_name}"
        return client


class Contract(models.Model):
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    contract_status = models.BooleanField(default=False, verbose_name="Signé")
    amount = models.FloatField(max_length=20, blank=True, null=True)
    payment_due = models.DateField()
    sales_contact = models.ForeignKey(User,
                                      on_delete=models.SET_NULL,
                                      null=True,
                                      blank=True,
                                      limit_choices_to={"team_id": 0})
    client = models.ForeignKey(Client,
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True)

    def __str__(self):
        if self.contract_status is False:
            stat = "En Négociation"
        else:
            stat = "Signé"
        return f"Le Contrat du client:{self.client} crée le:{self.date_created} est:{stat}"


class Event(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now=True)
    event_status = models.BooleanField(default=False, verbose_name="Terminé")
    attendees = models.PositiveIntegerField()
    event_date = models.DateTimeField()
    notes = models.TextField(null=True, blank=True)
    support_contact = models.ForeignKey(User,
                                        on_delete=models.SET_NULL,
                                        null=True,
                                        blank=True,
                                        limit_choices_to={"team_id": 1})
    contract = models.OneToOneField(Contract,
                                    on_delete=models.CASCADE,
                                    null=True,
                                    blank=True)

    def __str__(self):
        if self.event_status is False:
            stat = "En cours"
        else:
            stat = "Terminé"
        return f"L'évènement:{self.name} crée le:{self.date_created} est:{stat}"
