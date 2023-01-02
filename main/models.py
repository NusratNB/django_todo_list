from django.db import models

# Create your models here.

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    # description = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # completed = models.BooleanField(default=False)
