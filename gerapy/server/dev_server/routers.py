import os
from rest_framework.routers import DefaultRouter

from core import viewsets

router = DefaultRouter()
router.register('users', viewsets.UserViewSet)
router.register('spiders', viewsets.SpiderViewSet)
router.register('clients', viewsets.ClientViewSet)
router.register('projects', viewsets.ProjectViewSet)
