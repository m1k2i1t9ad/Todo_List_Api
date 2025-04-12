
from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')  # links todo to a user; deletes todos if user is deleted
    title = models.CharField(max_length=255)  # short title of the task
    description = models.TextField()  # detailed info about the task
    created_at = models.DateTimeField(auto_now_add=True)  # set once when created

    def __str__(self):
        return self.title  # shows title when printing the object

