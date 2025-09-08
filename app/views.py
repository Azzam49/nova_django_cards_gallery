from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def home(request):

    # # TODO: get the cards data from the model (database's table)
    # Dummy data / Hard coded data
    cards = [
        {
            "image": "img/landscape.jpeg",
            "title": "Beautiful Landscape",
            "description": "Experience the breathtaking beauty of nature with this stunning landscape photograph showcasing mountains and a calm lake.",
        },
        {
            "image": "https://images.unsplash.com/photo-1518837695005-2083093ee35b?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
            "title": "Urban Cityscape",
            "description": "Explore the vibrant energy of a modern city with its impressive architecture and bustling streets in this urban photography.",
        },
        {
            "image": "https://images.unsplash.com/photo-1518837695005-2083093ee35b?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
            "title": "Testing",
            "description": "Explore the vibrant energy of a modern city with its impressive architecture and bustling streets in this urban photography.",
        },
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
    ]
    # return HttpResponse("<h1>Hello</h1>")
    return render(request, 'app/home.html', {"cards": cards})

def about_us(request):
    return render(request, 'app/about_us.html', {})