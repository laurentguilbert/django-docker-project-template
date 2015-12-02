"""
Models for core.
"""
from django.db import models
from django.utils import timezone


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating 'created'
    and 'modified' fields.
    """
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created = timezone.now()
        self.modified = timezone.now()
        super(TimeStampedModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True
