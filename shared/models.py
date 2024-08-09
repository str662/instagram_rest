from django.db import models
import uuid


class BaseModel(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    created_time = models.DateField(auto_now_add=True)
    updated_time = models.DateField(auto_now=True)

    class Meta:
        abstract = True