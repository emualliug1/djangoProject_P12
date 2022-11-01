import dj_rest_auth.views
from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from authentification.views import UserViewSet, TeamViewSet
from api.views import ClientViewSet, ContractViewSet, EventViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

user_router = routers.DefaultRouter()
user_router.register('user', UserViewSet, basename='users')

client_router = routers.DefaultRouter()
client_router.register('client', ClientViewSet, basename='clients')

team_router = routers.DefaultRouter()
team_router.register('team', TeamViewSet, basename='teams')

contract_router = routers.NestedSimpleRouter(parent_router=client_router, parent_prefix='client', lookup='client')
contract_router.register('contract', ContractViewSet, basename='contracts')

event_router = routers.NestedSimpleRouter(parent_router=contract_router, parent_prefix='contract', lookup='contract')
event_router.register('event', EventViewSet, basename='events')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(user_router.urls)),
    path("api/", include(team_router.urls)),
    path("api/", include(client_router.urls)),
    path("api/", include(contract_router.urls)),
    path("api/", include(event_router.urls)),
    path("api/login/", dj_rest_auth.views.LoginView.as_view(), name='Login'),
    path("api/signup/", include('dj_rest_auth.registration.urls')),
    path("api/api-auth/", include("rest_framework.urls")),
    path("api/dj-rest-auth/", include("dj_rest_auth.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name='schema'),
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name='schema'), name="redoc"),
    path("api/schema/swagger/", SpectacularSwaggerView.as_view(url_name='schema'), name="swagger"),
]
