from django.urls import path

from tasks.views import TodoListListView, TodoItemListView, TodoListCreateView

urlpatterns = [
    path('', TodoListListView.as_view(), name='index'),
    path('list/<int:list_id>', TodoItemListView.as_view(), name='list'),
    path('list/add/', TodoListCreateView.as_view(), name='list-add'),
]
