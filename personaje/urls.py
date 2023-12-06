from django.urls import include, path
from .views import PersonajeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'personajes', PersonajeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
