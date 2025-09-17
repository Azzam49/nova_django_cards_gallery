from django.contrib import admin
from app.models import Card, TeamMember

# Register your models here.

@admin.register(Card) # registers the CardAdmin and link it with the Card model
class CardAdmin(admin.ModelAdmin):

    # list_display is used to display those columns on the django admin site
    list_display = [
        # "image",
        "title",
        "phone",
        "description",
    ]

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):


    list_display = [
        "name",
        "title",
        "age",
        "is_active"
    ]