from django.db import models


class BaseManager(models.Manager):
    def get_queryset(self):
        super().get_queryset().filter(is_deleted=False)
