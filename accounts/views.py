from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from accounts.models import User
from accounts.serializers import UserSerializer


class AccountsView(ModelViewSet):
    """ """

    http_method_names = ['get', 'post']
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        if self.request.method == 'POST':
            return [AllowAny()]
        else:
            return [IsAuthenticated()]

    def get_queryset(self):
        return User.objects.filter(username=self.request.user.username)