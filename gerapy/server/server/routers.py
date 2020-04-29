from rest_framework.routers import DefaultRouter

from gerapy.server.core.viewsets import (
    UserViewSet, SpiderViewSet, ProjectViewSet
)

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('spiders', SpiderViewSet)
router.register('projects', ProjectViewSet)
