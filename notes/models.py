from django.contrib.auth import get_user_model
from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    edited = models.DateField(auto_now=True, auto_now_add=False)
    created = models.DateField(auto_now=False, auto_now_add=True)
