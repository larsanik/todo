#from django.shortcuts import render
#from rest_framework import views
#from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions
from rest_framework import viewsets

from api.serializers import TodoListSerializer, TodoItemSerializer
from api.permissions import IsOwner, IsListOwner
from tasks.models import TodoList, TodoItem


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


class TodoItemViewset(viewsets.ModelViewSet):
    serializer_class = TodoItemSerializer
    queryset = TodoItem.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsListOwner]

    def filter_queryset(self, queryset):
        return queryset.filter(todo_list__owner=self.request.user)
