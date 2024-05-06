from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=1000)
    completed = models.BooleanField(default=False)
    expiry = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.task
    
    def save(self, *args, **kwargs):
        if not self.expiry:
            # Set expiry to 30 minutes from now if it's not already set
            self.expiry = timezone.now() + timedelta(minutes=30)
        super().save(*args, **kwargs)

