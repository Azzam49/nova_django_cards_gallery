from django.db import models

# Create your models here.
class Card(models.Model):
    image = models.CharField(max_length=300) # Default=required
    title = models.CharField(max_length=200) # Default=required
    description = models.CharField(max_length=500, blank=True, null=True) # Optional
    phone = models.CharField(max_length=150, blank=True, null=True)

    # This __str__ function, is a function that django expects.
    # It acts as the representation string for the models' record
    def __str__(self):
        return self.title # django will use the `title` column as representation string for each record

# Camel Case
class TeamMember(models.Model):
    # Text = CharField
    name = models.CharField(max_length=100) # required

    # Text = CharField
    title = models.CharField(max_length=200, blank=True, null=True) # optional

    # Number = IntegerField
    age = models.IntegerField() # no need to have max_length

    # Boolean (True ~ Yes/ False ~ No) = BooleanField
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.title}"