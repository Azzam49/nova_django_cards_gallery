from django.shortcuts import render
# from django.http import HttpResponse
from app.models import Card, TeamMember


# Create your views here.
def home(request):

    # Fetch all records from the Card model
    cards = Card.objects.all() # ORM Query (Object Relational Mapping)
    # cards is QuerySet datatype, you can treat it as list of dicts

    return render(request, 'app/home.html', {"cards": cards})



 # - cards is the output from `Card.objects.all()`
    # - cards contains all the cards from the Model
    # - cards have a special datatype known as `QuerySet`
    # - `QuerySet` datatype, is a dataype created by Django
    # - `QuerySet` datatype, is similiar to List datatype but with more features to serve Django records

    ########## Below is testing code, for displaying cards on terminal:
    # # i will loop over `cards` to print on my terminal all my cards
    # for card in cards:
    #     # card is a record from `cards`, it represents each card record from the Card Model
    #     print("")
    #     print("-"*20)
    #     print(f"image : {card.image}")
    #     print(f"title : {card.title}")
    #     print(f"description : {card.description}")
    #     print("-"*20)
    #     print("")
    ##########

    # Dummy data / Hard coded data
    # cards = [
    #     {
    #         "image": "img/landscape.jpeg",
    #         "title": "Beautiful Landscape",
    #         "description": "Experience the breathtaking beauty of nature with this stunning landscape photograph showcasing mountains and a calm lake.",
    #     },
    #     {
    #         "image": "https://images.unsplash.com/photo-1518837695005-2083093ee35b?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
    #         "title": "Urban Cityscape",
    #         "description": "Explore the vibrant energy of a modern city with its impressive architecture and bustling streets in this urban photography.",
    #     },
    #     {
    #         "image": "https://images.unsplash.com/photo-1518837695005-2083093ee35b?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
    #         "title": "Testing",
    #         "description": "Explore the vibrant energy of a modern city with its impressive architecture and bustling streets in this urban photography.",
    #     },
        # {
        #     "image": "https://images.unsplash.com/photo-1418065460487-3e41a6c84dc5?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
        #     "title": "Mystical Forest",
        #     "description": "Step into an enchanting forest filled with towering trees and dappled sunlight creating a magical atmosphere.",
        # },
        # {
        #     "image": "https://images.unsplash.com/photo-1465146344425-f00d5f5c8f07?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
        #     "title": "Serene Beach",
        #     "description": "Relax with this peaceful beach scene featuring gentle waves, soft sand, and a beautiful sunset on the horizon.",
        # },
        # {
        #     "image": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
        #     "title": "Majestic Mountains",
        #     "description": "Marvel at the grandeur of snow-capped mountain peaks against a clear blue sky in this breathtaking photograph.",
        # },
        # {
        #     "image": "https://images.unsplash.com/photo-1470115636492-6d2b56f9146d?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
        #     "title": "Wildlife Encounter",
        #     "description": "Get up close with nature's magnificent creatures in their natural habitat through this captivating wildlife photography.",
        # },
        # {
        #     "image": "https://images.unsplash.com/photo-1470115636492-6d2b56f9146d?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
        #     "title": "Tesing 123",
        #     "description": "Get up close with nature's magnificent creatures in their natural habitat through this captivating wildlife photography.",
        # },
    # ]

def about_us(request):
    return render(request, 'app/about_us.html', {})


def contact_us(request):
    cards = Card.objects.all() # Access all Cards data
    return render(request, 'app/contact_us.html', {"cards": cards}) # Passing data to contact_us HTML page


def testing(request):
    # QuerySet          # ORM Query
    # ORM Query = give us result as QuerySet
    # QuerySet = is the collection of data from our model

    # This ORM query fetch all the data from TeamMember.
    # team_members = TeamMember.objects.all()

    # Goal : Write different ORM Query, to meet our filtering needs.

    # 1 - Fetch only active team members (is_active = True)
    #   filter(`column_you_want_to_filter_by` = `value_you_want_to_filter_with`)
    #   filter() will return QuerySet, that have all the data that meets the conditon is_active=True
    # active_members = TeamMember.objects.filter(is_active = True)

    # 2 - Fetch only adult team members (age >= 18)
    # age__gte means this condition `age >= 18`
    # __gte stands for `greater than or equal to`
    # age__gte applies `age >= 18` for age column, to fetch only adult team members
    adult_members = TeamMember.objects.filter(age__gte = 18)

    # 3 - Fetch only team members that their (title includes `dev`)


    print(f"\nteam_members : {adult_members}\n")
    return render(request, 'app/Testing/testing.html', {"team_members": adult_members})