from django.db import models
from django.core.validators import validate_email

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