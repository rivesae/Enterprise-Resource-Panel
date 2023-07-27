import uuid
from django.db import models
from core.models import CustomUser
from django.utils import timezone

class Document(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    document_ref = models.IntegerField(null=True, blank=True)
    source = models.CharField(max_length=255, null=True, blank=True)
    source_href = models.CharField(max_length=255, null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    created = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='dateandtime_created')
    date_deleted = models.DateTimeField(null=True, blank=True)
    deleted = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='dateandtime_deleted')