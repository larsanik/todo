from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from tasks.models import TodoList


# Create your views here.
class TodoListListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('account_login')
    template_name = 'task/index.html'

    def get_queryset(self):
        return TodoList.objects.for_user(self.request.user)
