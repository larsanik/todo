from django.contrib import admin

from tasks.models import TodoList, TodoItem

# Register your models here.
admin.site.register(TodoList)
admin.site.register(TodoItem)
