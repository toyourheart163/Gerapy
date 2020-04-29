from rest_framework.routers import DefaultRouter

from gerapy.server.core.viewsets import (
    UserViewSet, SpiderViewSet, ProjectViewSet, ClientViewSet
)

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('spiders', SpiderViewSet)
router.register('projects', ProjectViewSet)
router.register('clients', ClientViewSet)
