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


class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300, blank=True, null=True) # optional

    def __str__(self):
        return f"{self.name}"


class TeamMember(models.Model):
    # Text/String = CharField
    name = models.CharField(max_length=100) # required

    # Text/String = CharField
    title = models.CharField(max_length=200, blank=True, null=True) # optional

    # Number = IntegerField
    age = models.IntegerField() # no need to have max_length # required

    # Boolean (True ~ Yes/ False ~ No) = BooleanField
    is_active = models.BooleanField(default=True) # required

    # ============================================
    # FOREIGNKEY: Each TeamMember belongs to a single Department
    # ============================================
    #
    # Syntax: department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    #
    # What this means:
    # - Each TeamMember MUST belong to ONE Department
    # - You can have many TeamMembers in the same Department
    # - If a Department is deleted, all its TeamMembers are deleted too (CASCADE)


    # Examples of usage:
    #   1. Creating a TeamMember with a department:
    #      dept = Department.objects.get(name="Engineering")
    #      TeamMember.objects.create(name="John", age=25, department=dept)
    #
    #   2. Getting a TeamMember's department:
    #      member = TeamMember.objects.get(id=1)
    #      print(member.department.name)  # Prints: "Engineering"
    #
    #   3. Getting all TeamMembers in a department:
    #      dept = Department.objects.get(name="Engineering")
    #      members = dept.teammember_set.all()  # Get all TeamMembers in this department
    # ============================================
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE, # on_delete parameter with CASCADE value, makes this behviour : If a Department is deleted, all its TeamMembers are deleted too (CASCADE)
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.name} - {self.title}"


