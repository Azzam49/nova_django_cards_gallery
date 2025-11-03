from django.contrib import admin
from app.models import Card, TeamMember, Department

# Register your models here.

@admin.register(Card) # registers the CardAdmin and link it with the Card model
class CardAdmin(admin.ModelAdmin):

    # list_display is used to display those columns on the django admin site
    list_display = [
        "id",
        # "image",
        "title",
        "phone",
        "description",
    ]

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):


    list_display = [
        "id",
        "name",
        "title",
        "age",
        "is_active",
        "department"
    ]


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):


    list_display = [
        "id",
        "name",
        "description",
    ]