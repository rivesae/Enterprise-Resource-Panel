from django.db import models
from django.utils import timezone

class Update(models.Model):
    version = models.CharField(max_length=7)
    comment = models.TextField()
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.version