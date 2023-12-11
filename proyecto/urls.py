from django.urls import include, path
from .views import ProyectoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'proyectos', ProyectoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
