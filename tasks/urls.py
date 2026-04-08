from django.urls import path

from tasks.views import TodoListListView, TodoItemListView

urlpatterns = [
    path('', TodoListListView.as_view(), name='index'),
    path('list/<int:list_id>', TodoItemListView.as_view(), name='list'),
]
