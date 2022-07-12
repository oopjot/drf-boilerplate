from django.db import models
from uuid import uuid4


class TimeStampAbstractModel(models.Model):
    """
    Provides two datetime fields:
    - created at
    - upated_at
    """

    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UUIDAbstractModel(models.Model):
    """
    Provides unique UUID field
    """

    class Meta:
        abstract = True

    uuid = models.UUIDField(unique=True, default=uuid4)
