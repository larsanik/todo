from django.urls import path, include
from api.views import TodoListListCreateView, TodoListRetrieveUpdateDestroyView, TodoItemViewset
from rest_framework import routers

router = routers.DefaultRouter()

router.register('items', TodoItemViewset, basename='item')


urlpatterns = [
    path('', include(router.urls)),
    path('lists/', TodoListListCreateView.as_view()),
    path('lists/<int:pk>/', TodoListRetrieveUpdateDestroyView.as_view()),
]
