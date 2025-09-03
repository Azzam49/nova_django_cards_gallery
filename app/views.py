from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("<h1>Hello</h1>")
    return render(request, 'app/home.html', {})

def about_us(request):
    return render(request, 'app/about_us.html', {})