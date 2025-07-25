from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from core.managers import BaseManager


class BaseDBModel(models.Model):
    """
    Base DB model from which all other DB models should inherit.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    objects = BaseManager()
    objects_including_deleted = models.Manager()

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save(update_fields=["is_deleted"])


class User(BaseDBModel, AbstractUser):
    pass
