from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from rest_framework import generics

from api.serializers import TodoListSerializer
from tasks.models import TodoList


# Create your views here.
class TodoListListView(generics.ListAPIView):
    serializer_class = TodoListSerializer
    queryset = TodoList.objects.all()

# Переписали через rest_framework  generics и то что ниже уже не нужно
#class TodoListListView(views.APIView):
    # def get(self, request, **kwargs):
    #     todo_list = TodoList.objects.all()
    #     serialized = TodoListSerializer(todo_list, many=True)
    #     return Response(serialized.data)
