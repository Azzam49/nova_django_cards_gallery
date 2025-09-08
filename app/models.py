from django.db import models

# Create your models here.
class Card(models.Model):
    image = models.CharField(max_length=300) # Default=required
    title = models.CharField(max_length=150) # Default=required
    description = models.CharField(max_length=500, blank=True, null=True) # Optional