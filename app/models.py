from django.db import models

# Create your models here.
class Card(models.Model):
    image = models.CharField(max_length=300) # Default=required
    title = models.CharField(max_length=150) # Default=required
    description = models.CharField(max_length=500, blank=True, null=True) # Optional

    # This __str__ function, is a function that django expects.
    # It acts as the representation string for the models' record
    def __str__(self):
        return self.title # django will use the `title` column as representation string for each record