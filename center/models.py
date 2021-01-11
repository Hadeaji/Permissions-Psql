from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Center(models.Model):
    name = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    employee = models.CharField(max_length=64)
    anouncment = models.TextField()

    def __str__(self):
        return str(self.name)