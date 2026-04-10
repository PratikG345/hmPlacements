from django.db import models

# Create your models here.

class Requirement(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=15)
    workforce = models.CharField(max_length=100)
    requirement = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name