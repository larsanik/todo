from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from tasks.models import TodoList, TodoItem
from django.core.exceptions import PermissionDenied


# Create your views here.
class TodoListListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('account_login')
    template_name = 'tasks/index.html'

    def get_queryset(self):
        return TodoList.objects.for_user(self.request.user)

class TodoItemListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('account_login')
    template_name = 'tasks/todo_list.html'

    def get_queryset(self):
        todo_list = TodoList.objects.for_user(self.request.user).filter(pk=self.kwargs['list_id'])
        if todo_list is None:
            raise PermissionDenied()
        return TodoItem.objects.filter(todo_list_id=self.kwargs['list_id'])

class TodoListCreateView(LoginRequiredMixin, CreateView):
    model = TodoList
    fields = ['title']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)