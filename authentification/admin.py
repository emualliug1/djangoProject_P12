from django.contrib import admin
from authentification.models import User, Team


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')


class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'team')


admin.site.register(User, UserAdmin)
admin.site.register(Team, TeamAdmin)
