from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework.exceptions import PermissionDenied

TEAM_CHOICES = [
    ('VENTE', 'Vente'),
    ('SUPPORT', 'Support'),
    ('GESTION', 'Gestion')
]


class Team(models.Model):
    team = models.CharField(max_length=15,
                            choices=TEAM_CHOICES,
                            null=True,
                            blank=True,)

    def delete(self, using=None, keep_parents=False):
        if User.is_superuser:
            super(Team, self).delete()
        else:
            raise PermissionDenied('Accès Refusé')

    def save(self, *args, **kwargs):
        if User.is_superuser:
            super(Team, self).save()
        else:
            raise PermissionDenied('Accès Refusé')

    def __str__(self):
        if self.team == 'VENTE':
            return f'{TEAM_CHOICES[0][1]}'
        elif self.team == 'SUPPORT':
            return f'{TEAM_CHOICES[1][1]}'
        else:
            return f'{TEAM_CHOICES[2][1]}'


class User(AbstractUser):
    team = models.ForeignKey(Team,
                             on_delete=models.PROTECT,
                             blank=True,
                             null=True,
                             related_name='users')

    def __str__(self):
        return f'{self.username}'


