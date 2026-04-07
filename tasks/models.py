from django.db import models

from users.models import User


# Create your models here.
class TodoList(models.Model):
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class TodoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)

    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} due: {self.date if self.due_date else 'whenever'}"
