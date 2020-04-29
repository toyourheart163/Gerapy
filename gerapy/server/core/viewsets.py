'''
viewsets user spider project
'''

from rest_framework import viewsets, permissions

from .permissions import IsOwnerOrReadOnly
from .serializers import (
    User, UserSerializer,
    Spider, SpiderSerializer,
    Client, ClientSerializer,
    Project, ProjectSerializer)


class UserViewSet(viewsets.ModelViewSet):
    '''regiter user or create user'''
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action == "retrieve":
            return [permissions.IsAuthenticated()]
        elif self.action == "create":
            return []
        return [permissions.IsAdminUser()]


class SpiderViewSet(viewsets.ModelViewSet):
    queryset = Spider.objects.filter(project__open=True)
    serializer_class = SpiderSerializer
    permission_classes = [IsOwnerOrReadOnly]


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticated]


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticated]
