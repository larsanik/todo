from django.urls import path
from api.views import TodoListListView

urlpatterns = [
    path('lists/', TodoListListView.as_view()),
]
