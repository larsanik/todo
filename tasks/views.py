from django import forms
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView
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

    def get_context_data(self, *,object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        todo_list=TodoList.objects.get(pk=self.kwargs['list_id'])
        context['todo_list'] = todo_list
        return context


class TodoListCreateView(LoginRequiredMixin, CreateView):
    model = TodoList
    fields = ['title']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class TodoItemCreateView(LoginRequiredMixin, CreateView):
    model = TodoItem
    fields = ['todo_list', 'title', 'description', 'due_date']

    def get_initial(self):
        initial_data = super().get_initial()
        todo_list = TodoList.objects.for_user(user=self.request.user).get(id=self.kwargs['list_id'])
        initial_data['todo_list'] = todo_list
        return initial_data

    def get_success_url(self):
        return reverse('list', args=[self.object.todo_list_id])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        todo_list = TodoList.objects.for_user(self.request.user).get(id=self.kwargs["list_id"])
        context["todo_list"] = todo_list
        context["title"] = "Создать новую задачу"
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['due_date'].widget = forms.SelectDateWidget()
        return form


class TodoItemUpdateView(LoginRequiredMixin, UpdateView):
     model = TodoItem
     fields = ['todo_list', 'title', 'description', 'due_date']

     def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context['todo_list'] = self.object.todo_list
         context['title'] = 'Редактировать задачу'
         return context

     def get_success_url(self):
         return reverse('list', args=[self.object.todo_list_id])
