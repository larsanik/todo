#from django.shortcuts import render
#from rest_framework import views
#from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions

from api.serializers import TodoListSerializer
from api.permissions import IsOwner
from tasks.models import TodoList


# Create your views here.
class TodoListListCreateView(generics.ListCreateAPIView):
    serializer_class = TodoListSerializer
    queryset = TodoList.objects.all()
    permission_classes = [permissions.IsAuthenticated] # добавили проверку аутентификации пользователя

    def filter_queryset(self, queryset):
        return queryset.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TodoListRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoListSerializer
    queryset = TodoList.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwner]

