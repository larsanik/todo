from django.urls import path
from api.views import TodoListListCreateView, TodoListRetrieveUpdateDestroyView

urlpatterns = [
    path('lists/', TodoListListCreateView.as_view()),
    path('lists/<int:pk>/', TodoListRetrieveUpdateDestroyView.as_view()),
]
