from django.db import models
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.utils import timezone

class Subscriber(models.Model):
    name = models.CharField(blank=True, max_length=255)
    email = models.EmailField(
        max_length=255,
        validators=[validate_email],
        unique=True
    )
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title