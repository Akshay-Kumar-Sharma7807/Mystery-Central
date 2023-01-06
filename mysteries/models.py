from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.TextField(blank=True)
    skills = models.ManyToManyField('Skill', blank=True)
    recent_mysteries = models.ManyToManyField('Mystery', blank=True)

class Skill(models.Model):
    name = models.CharField(max_length=50)


class Mystery(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    clues = models.TextField()
    is_solved = models.BooleanField(default=False)
    solution = models.TextField()

class Answer(models.Model):
    answer = models.TextField()
    correct = models.BooleanField(default=True)
    reviewed = models.BooleanField(default=False)
    answered_by = models.ForeignKey(User, on_delete=models.CASCADE)
    mystery = models.ForeignKey(Mystery, on_delete=models.CASCADE)
