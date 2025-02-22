from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import UserViewSet

router_v1 = DefaultRouter()
router_v1.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router_v1.urls)),
    path('auth/', include('djoser.urls.authtoken')),
]
