from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Property(models.Model):
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.key


class Entity(models.Model):
    modified_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="entities", null=True, blank=True
        )
    value = models.IntegerField()
    properties = models.ManyToManyField(
        Property, related_name="properties"
        )

    def __str__(self):
        return f"{self.value}"
