from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    titlu = models.CharField(max_length=50)
    descriere = models.TextField()
    completat = models.BooleanField(default=False)
    prioritate = models.BooleanField(default=False)
    data_creare = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titlu