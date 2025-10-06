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
    # adult_members = TeamMember.objects.filter(age__gte = 18)

    # 3 - Fetch only teenagers and kids team members (age < 18)
    # age__lt means this condition `age < 18`
    # __lt stands for `less than`
    # kids_and_teenagers_members = TeamMember.objects.filter(age__lt = 18)

    # Summary of Comparsion Operator for IntgerField
        # __gte means greater than or equal to
        # __lte means less than or equal to
        # __gt means greater than
        # __lt means less than

    # 4 - Fetch team members that have title as "Developer"
    # Fetch team members that the title value is exactly "Developer" (case sensetive)
        # will fetch for `title = "Developer"`
        # will not fetch for `title = "developer"`
    # We are using string value, because title on TeamMember is CharField
    # developer_members = TeamMember.objects.filter(title = "Developer")


    # 5 - Fetch only team members that their (title includes `De`)
    # Fetch all team members that includes `De` on the title
        # in our case will fetch (title as 'Developer' and 'Designer')
        # will not fetch title as 'Customer Service'
    # __icontains filter by partial value from the title column
    # title_contains_De = TeamMember.objects.filter(title__icontains = "De")


    # 6 - Fetch only team members that age is between (18 - 30)
    # To achieve this:
        # 1 - check for (age greater than or equal to 18) (age >= 18)
            # age__gte = 18
        # 2 - check for (age less than or equal to 30) (age <= 30)
            # age__lte = 30
    # age_between_18_and_30 = TeamMember.objects.filter(age__gte = 18, age__lte = 30)
        # .filter(age__gte = 18, age__lte = 30)
            # the comma means `AND`:
                # age__gte = 18 AND age__lte = 30

    # 7 - Fetch team members that title is `Developer` and age is between 6-10
    # kids_developer_member = TeamMember.objects.filter(
    #     age__gte = 6,
    #     age__lte = 10,
    #     title = "Developer"
    # )

    # 8 - Fetch team members that does not have any title (blank title)
        # title__isnull=True this will fetch (team members that DON'T have title - blank)
        # title__isnull=False this will fetch (team members that DO have title - not blank)
        # __isnull helps us to look for if column have or not have value
    # blank_title_members = TeamMember.objects.filter(title__isnull = True)


    # 9 - Fetch all team members - but exclude team members that has title='Developer'
    # non_developer_members = TeamMember.objects.exclude(title = 'Developer')
        # This was fetching both Alice and John
            # Alice , title = blank
            # John, title = 'Developer'

    # 10 - Fetch all team members that DO have a title (not blank) - but exclude team members that has title='Developer'
    # non_developer_members_that_have_title = TeamMember.objects.exclude(title = 'Developer').filter(title__isnull=False)
        # Fetch only John, because Alice does not have a title


    # 11 - ORDERING/SORTNG results
    # all_members = TeamMember.objects.all().order_by("age") # Sort by "age" column in ascending (numbers smallest to largest)
    # all_members = TeamMember.objects.all().order_by("-age") # Sort by "age" column in descending (numbers largest to smallest)
    # all_members = TeamMember.objects.all().order_by("name") # Sort by "name" column in ascending (from A to Z)
    # all_members = TeamMember.objects.all().order_by("-name") # Sort by "name" column in descending (from Z to A)
    # all_members = TeamMember.objects.all().order_by("is_active") # Sort by "is_active" column in ascending (Show False first and then True)
    # all_members = TeamMember.objects.all().order_by("-is_active") # Sort by "is_active" column in descending (Show True first and then False)
    # all_members = TeamMember.objects.all().order_by("-is_active", "-name")

    # 12 - Limiting Data
    # first_two = TeamMember.objects.all().order_by("-age")[0:2]
    next_two = TeamMember.objects.all().order_by("-age")[2:4]


    # 13 - Picking Specfic columns (For performance wise)
    # values() : will fetch specfic columns
    # as_dicts = TeamMember.objects.values("name", "age") # list of dicts
    # as_dicts = TeamMember.objects.all().values("name", "age", "is_active", "title") # list of dicts , eg :  # <QuerySet [{'name': 'Adam', 'age': 10}, {'name': 'John', 'age': 8}, {'name': 'Alice', 'age': 30}, {'name': 'Ben', 'age': 35}, {'name': 'Henry', 'age': 32}, {'name': 'Zen', 'age': 15}]>
    
    
    # 14 - Picking just list of values
    # list_of_tuples = TeamMember.objects.all().values_list("name", "age") # list of tuples eg : <QuerySet [('Adam', 10), ('John', 8), ('Alice', 30), ('Ben', 35), ('Henry', 32), ('Zen', 15)]>
    # all_names_as_list = TeamMember.objects.all().values_list("name", flat=True) # list of names, eg : <QuerySet ['Adam', 'John', 'Alice', 'Ben', 'Henry', 'Zen']>
    # all_names_as_list = list(TeamMember.objects.all().values_list("name", flat=True)) # eg : ['Adam', 'John', 'Alice', 'Ben', 'Henry', 'Zen']

    # sales = Sales.objects.all().values("sales_price")[:100000] # 3 sec
    # sales = Sales.objects.all()[:100000] # 12 sec


    # 15 - Counting Data

    ############ Counting all Members ############
    # all_members = TeamMember.objects.all() # eg:  <QuerySet [<TeamMember: Alice - Designer>, <TeamMember: Zen - Customer Service>]>
    # 1 :
    # members_count = TeamMember.objects.all().count() # eg: 6
    # 2 :
    # members_count = all_members.count() # eg: 6
    ############ Counting all Members ############


    ############ Counting Developer Members ############
    dev_members = TeamMember.objects.filter(title = "Developer")
    dev_members_count = dev_members.count()
    # dev_members_count = TeamMember.objects.filter(title = "Developer").count()
    ############ Counting Developer Members ############



    context = {
        "team_members": dev_members,
        "members_title": "Team Members",
        "members_count": dev_members_count,
    }
    return render(request, 'app/Testing/testing.html', context)