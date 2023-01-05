from django.db import models
from django.contrib.auth.models import User

class Mystery(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_solved = models.BooleanField(default=False)
