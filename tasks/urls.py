from django.urls import path

from tasks.views import TodoListListView

urlpatterns = [
    path('', TodoListListView.as_view(), name='list'),
]
