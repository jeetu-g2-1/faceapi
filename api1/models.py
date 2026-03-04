from django.db import models

# Create your models here.

class APIKey(models.Model):
    name=models.CharField(max_length=100)
    hashed_key=models.CharField(max_length=128, unique=True)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
